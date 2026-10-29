"""Independent, read-only output checks; never import or execute the producer.

Energy derivatives use closed trigonometric coefficients, not Fourier convolution.
Hermite polynomials use their factorial sum, not the producer's recurrence.
Only this audit directory receives a newly written verification report.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import csv
import hashlib
import json
import platform

ROOT = Path(__file__).resolve().parents[2]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def q(row, name):
    return Q(row[name])


def demand(row, name, expected):
    assert q(row, name) == expected, (name, row.get('case'), row[name], str(expected))


def energy(row):
    m, n = row['m'], row['n']
    a, b, h = (q(row, k) for k in ('A_x_amplitude', 'A_y_amplitude', 'N_amplitude'))
    te, ti, d, den, kap, G = (q(row, k) for k in ('Te', 'Ti', 'de_squared', 'n0', 'kappa', 'G'))
    alpha = kap * G / den
    exchange = h * a * b * m * n * (m*m-n*n) / 4
    # Trigonometric expansion: only the original cosine modes can enter Udot/Kedot.
    axdot = -kap*b*h*m*n*(te+ti+ti*d*n*n) / (2*(1+d*m*m))
    aydot = kap*a*h*m*n*(te+ti+ti*d*m*m) / (2*(1+d*n*n))
    udot = G*(m*m*a*axdot+n*n*b*aydot)/2
    kedot = G*d*(m**4*a*axdot+n**4*b*aydot)/2
    kidot, ydot = den*ti*alpha*exchange, den*te*alpha*exchange
    # Six distinct cosine modes have squared means 1/2. Coefficients are
    # C/2,-C/4,-C/4 and -D/2,D/4,D/4, so the squared norm is 3(C^2+D^2)/16.
    C, D = a*h*m**3*n, b*h*m*n**3
    inertia_norm = (kap*ti*d)**2 * Q(3,16)*(C*C+D*D)
    expected = {
        'alpha': alpha, 'I': exchange,
        'U': G*(m*m*a*a+n*n*b*b)/4,
        'Ke': G*d*(m**4*a*a+n**4*b*b)/4,
        'Ki': den*ti*h*h/8, 'Y_half': den*te*h*h/8,
        'U_dot': udot, 'Ke_dot': kedot, 'Ki_dot': kidot, 'Y_half_dot': ydot,
        'consistent_total_dot': udot+kedot+kidot+ydot,
        'printed_double_density_total_dot': udot+kedot+kidot+2*ydot,
        'isolated_main_continuity_sign_total_dot': udot+kedot-kidot-ydot,
        'inertial_advection_Fdot_squared_norm': inertia_norm,
        'ion_to_printed_density_ratio': ti/(2*te),
        'ion_to_consistent_density_ratio': ti/te,
    }
    for name, value in expected.items():
        demand(row, name, value)
    assert expected['consistent_total_dot'] == 0
    assert udot+kedot == -G*kap*(te+ti)*exchange
    assert (exchange == 0) == (expected['printed_double_density_total_dot'] == 0)
    return exchange != 0


def H(m):
    # Physicists' Hermite explicit factorial formula; independent of recurrence.
    p = [Q(0)]*(m+1)
    for j in range(m//2+1):
        power = m-2*j
        p[power] = Q((-1)**j*factorial(m)*2**power, factorial(j)*factorial(power))
    return p


def moment(power):
    return Q(0) if power%2 else Q(factorial(power), 4**(power//2)*factorial(power//2))


def inner(p, r, shift=0):
    return sum((a*b*moment(i+j+shift) for i,a in enumerate(p) for j,b in enumerate(r)), Q(0))


def hermite(report):
    polynomials = [H(m) for m in range(9)]
    assert [[str(x) for x in p] for p in polynomials] == report['physicists_Hermite_coefficients']
    assert len(report['orthogonality_checks']) == 81
    for row in report['orthogonality_checks']:
        m, n = row['m'], row['n']
        value = inner(polynomials[m],polynomials[n])
        assert value == (2**m*factorial(m) if m==n else 0)
        demand(row,'value',value)
    for row in report['drive_projections']:
        m = row['m']
        demand(row,'unnormalized_projection',inner(polynomials[m],[Q(1),Q(0),Q(-2)]))
        demand(row,'normalization_squared',Q(2**m*factorial(m)))
    assert len(report['drive_projections']) == 9
    assert Q(report['g2_drive_in_units_sqrt2']) == -1
    assert Q(report['printed_Eq11_g2_drive_in_units_sqrt2']) == 1
    for row in report['streaming_pairs']:
        m,n = row['m'],row['neighbor']
        assert n==m+1
        value = inner(polynomials[m],polynomials[n],1)
        demand(row,'normalized_coefficient_squared',value**2/Q(2**(m+n)*factorial(m)*factorial(n)))
        assert Q(row['normalized_coefficient_squared']) == Q(m+1,2)
        assert row['Eq9_RHS_streaming_sign']==-1 and row['printed_Eq11_RHS_streaming_sign']==1
    assert len(report['streaming_pairs']) == 6


def rate(row):
    te,ti,me,mi,den,bg,bp,r = (q(row,k) for k in ('Te','Ti','me','mi','n0','B0','Bperp','R'))
    de2 = me/den  # c=e=1 and the declared absorbed 4*pi convention.
    va2 = bp*bp/(den*mi)
    rho2 = te*mi/(bg*bg)
    tau2 = me*bg*bg*r*r/((te+ti)*bp*bp)
    life2 = r*r*tau2/de2
    rate2 = r*r/(va2*life2)
    beta = 2*den*ti/(bg*bg)
    thermal = 1+te/ti
    ermhd = beta*thermal/(2+beta*thermal)*(mi/den)/(r*r)
    for name,val in {
        'de_squared':de2,'rhos_squared':rho2,'tau_squared':tau2,
        'reconnection_tau_squared':life2,'main_Eq4_rate_squared':rate2,
        'main_Eq5_rate_squared':de2/(r*r),'beta_i':beta,
        'supplement_Eq3_rate_squared':ermhd,
        'ERMHD_to_lowbeta_squared_rate_ratio':2/(2+beta*thermal),
    }.items():
        demand(row,name,val)
    assert rate2 == (te+ti)*mi/(bg*bg*r*r)
    assert ermhd/rate2 == 2/(2+beta*thermal)


def compare_csv(path, rows):
    with path.open(encoding='utf-8',newline='') as f:
        actual = list(csv.DictReader(f))
    assert len(actual) == len(rows)
    for saved, source in zip(actual, rows):
        assert set(saved) == set(source)
        for k,v in source.items():
            expected = '' if v is None else str(v)
            assert saved[k] == expected, (path.name,k,saved[k],expected)


def main():
    if not __debug__:
        raise RuntimeError('Independent exact checks require assertions; -O is not supported.')
    names = [
        'reproduction/run_audit.py','data/equation-controls.json',
        'data/periodic-energy-controls.csv','data/linear-symbol-controls.csv',
        'data/retained-rate-controls.csv','data/conditional-exponents.csv',
        'data/runtime-environments.json','figures/energy-and-wave-controls.png',
        'figures/hermite-projection-controls.png','COMPUTATIONAL_METHODS.md',
        'README.md','REPRODUCIBILITY.md','requirements.txt','LICENSE-CODE',
        'LICENSE-MANUSCRIPT','source-provenance.json','SOURCE_CONCORDANCE.md',
        'audit/source-integration-verification.json','audit/source-record-copy-manifest.json',
    ]
    manifest = json.loads((ROOT/'audit/source-record-copy-manifest.json').read_text(encoding='utf-8'))
    assert manifest['original_record_count'] == len(manifest['files']) == 24
    for entry in manifest['files']:
        file = ROOT/entry['package_path']
        assert file.stat().st_size == entry['bytes'] and digest(file) == entry['SHA256']
        if entry['package_path'] not in names:
            names.append(entry['package_path'])
    before = {name:digest(ROOT/name) for name in names}
    doc = json.loads((ROOT/'data/equation-controls.json').read_text(encoding='utf-8'))
    assert doc['producer_sha256'] == before['reproduction/run_audit.py']
    assert len(doc['energy']) == 60
    observed = {(row['m'],row['n'],q(row,'A_x_amplitude'),q(row,'A_y_amplitude'),q(row,'N_amplitude'),
                 q(row,'Te'),q(row,'Ti'),q(row,'de_squared')) for row in doc['energy']}
    expected = {(m,n,a,b,h,te,ti,d)
                for m,n,a,b,h in [(1,2,Q(1),Q(1),Q(1)),(2,3,Q(1,2),Q(2),Q(-1)),
                                  (3,1,Q(2),Q(1,3),Q(3,2)),(1,1,Q(1),Q(1),Q(1)),(1,2,Q(0),Q(1),Q(1))]
                for te,ti in [(Q(1),Q(1)),(Q(1,2),Q(2)),(Q(3),Q(1,3)),(Q(2),Q(3))]
                for d in [Q(0),Q(1,4),Q(2)]}
    assert observed == expected and len(observed)==60
    nonzero = sum(energy(row) for row in doc['energy'])
    assert nonzero == 36
    for row in doc['linear']:
        g,te,ti,d,kp,kz,me = (q(row,k) for k in ('Gamma0_symbol','Te','Ti','de_squared','kperp_squared','kparallel_squared','me'))
        # Derive the two off-diagonal phase-pair coefficients separately.
        a_times_b = d*kp*kz*(te+ti/(1-g))/(me*(1+d*kp))
        for name,sign in [('consistent_omega_squared',1),('literal_main_lambda_squared',1),('consistent_lambda_squared',-1)]:
            demand(row,name,sign*a_times_b)
        assert a_times_b>0 and row['pressure_coefficient_restored_before_sign_isolation']
    assert len(doc['linear'])==24
    hermite(doc['hermite'])
    for row in doc['retained_rate_controls']:
        rate(row)
    assert len(doc['retained_rate_controls'])==8
    for row in doc['retained_conditional_exponents']:
        s = q(row,'lifetime_R_power_at_fixed_B')
        et = -Q(2)/(s+1)
        for name,value in {'decay_ODE_energy_power':(s+3)/2,'energy_time_power':et,
                           'radius_time_power':-et/2,'field_time_power':et/2,'wavenumber_time_power':et/2}.items():
            demand(row,name,value)
        if row['regime']=='electron_only':
            demand(row,'critical_balance_length_time_power',-et)
        else:
            assert row['critical_balance_length_time_power'] is None
    dim = doc['dimensional']
    assert tuple(a+b for a,b in zip(dim['bare_parallel_density_gradient'],dim['missing_cTe_over_e'])) == tuple(dim['A_time_derivative'])
    assert dim['bare_parallel_density_gradient'] != dim['A_time_derivative']
    for filename,key in [('periodic-energy-controls.csv','energy'),('linear-symbol-controls.csv','linear'),
                         ('retained-rate-controls.csv','retained_rate_controls'),('conditional-exponents.csv','retained_conditional_exponents')]:
        compare_csv(ROOT/'data'/filename,doc[key])
    runtime = json.loads((ROOT/'data/runtime-environments.json').read_text(encoding='utf-8'))
    assert runtime['producer_sha256'] == before['reproduction/run_audit.py']
    for name,value in (runtime['exact_output_sha256'] | runtime['figures']).items():
        assert digest(ROOT/name) == value
    assert before == {name:digest(ROOT/name) for name in names}
    result = {
        'status':'passed','reviewer_role':'independent source and derivation reviewer',
        'method':'Read-only standard-library calculations; no import or execution of producer or another verifier. Closed trigonometric coefficients replace Fourier convolution; explicit factorial Hermite polynomials replace recurrence.',
        'python':platform.python_version(),'verifier_sha256':digest(Path(__file__)),
        'counts':doc['counts'],'all_four_CSVs_equal_JSON':True,
        'all_24_original_record_copies_match_manifest':True,
        'all_bound_inputs_byte_unchanged':True,'input_sha256':before,
        'scope':'Synthetic displayed-equation identities only; no source simulation, VOR, final journal supplement, time-integrated nonlinear evolution or diagnostic reanalysis.',
    }
    (Path(__file__).parent/'checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'status':'passed','counts':doc['counts'],'bound_input_count':len(before)}))


if __name__=='__main__':
    main()
