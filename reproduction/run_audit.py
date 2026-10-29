"""Original exact controls for named printed electron-only model equations.

This is not a plasma simulation, a source-code reproduction, or a VOR audit.
All equation checks use standard-library Fraction arithmetic. Matplotlib/NumPy
are imported only when drawing two explicitly synthetic explanatory figures.
No independent verifier or source program is imported or executed.
"""
from __future__ import annotations

import argparse
import csv
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
TITLE = 'Equation consistency in electron-only reconnection'
SOURCE = {
    'title': 'Electron-only magnetic reconnection and inverse magnetic-energy transfer at sub-ion scales',
    'arxiv': '2407.06020v2',
    'journal_DOI': '10.1103/PhysRevLett.134.155201',
    'arxiv_v2_PDF_sha256': 'e482988aa241494c52cc6071317fbd6f3a1c084173f045f2bfc03ba0ade26cd8',
    'publisher_accepted_manuscript_PDF_sha256': '71c9216d20334427fdc84570c72b600c82c7009721f03837787f8d5a74eadd83',
    'arxiv_v2_main_tex_sha256': 'a0684bc516404d59ebe488b092ee08c062a1273ccad8e785b82c01fdffdd7f81',
    'identity_semantics': 'Recorded source identities, not rehashed by this offline program. The authentic CHORUS accepted manuscript is not the uninspected subscription VOR. Supplement checks refer only to arXiv v2.',
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def tidy(field):
    return {key: F(value) for key, value in field.items() if value}


def add(*fields):
    out = {}
    for field in fields:
        for key, value in field.items():
            out[key] = out.get(key, F(0)) + value
    return tidy(out)


def scale(field, factor):
    return tidy({key: value * factor for key, value in field.items()})


def product(f, g):
    out = {}
    for p, fp in f.items():
        for q, gq in g.items():
            k = (p[0] + q[0], p[1] + q[1])
            out[k] = out.get(k, F(0)) + fp * gq
    return tidy(out)


def bracket(f, g):
    """Real Fourier convolution: two factors i give minus cross(p,q)."""
    out = {}
    for p, fp in f.items():
        for q, gq in g.items():
            k = (p[0] + q[0], p[1] + q[1])
            out[k] = out.get(k, F(0)) - (p[0] * q[1] - p[1] * q[0]) * fp * gq
    return tidy(out)


def laplacian(f):
    return tidy({k: -(k[0] ** 2 + k[1] ** 2) * value for k, value in f.items()})


def mean_product(f, g):
    return sum((v * g.get((-k[0], -k[1]), F(0)) for k, v in f.items()), F(0))


def cosine(kx, ky, amplitude=F(1)):
    return {(kx, ky): amplitude / 2, (-kx, -ky): amplitude / 2}


def sine_product(m, n, amplitude=F(1)):
    # sin(mx)sin(ny) = [cos(mx-ny)-cos(mx+ny)]/2.
    return add(cosine(m, -n, amplitude / 2), cosine(m, n, -amplitude / 2))


def energy_case(m, n, a, b, density_amplitude, Te, Ti, de2, n0, kappa):
    A = add(cosine(m, 0, a), cosine(0, n, b))
    N = sine_product(m, n, density_amplitude)
    L = laplacian(A)
    potential = scale(N, -Ti)  # normalized e=1, strict-subion closure.
    generalized_flux = add(A, scale(L, -de2))
    # Full Appendix A2 advection retained, including de^2{Delta A,N}.
    flux_dot = add(scale(bracket(potential, generalized_flux), -kappa),
                   scale(bracket(A, N), -kappa * Te))
    A_dot = {k: v / (1 + de2 * (k[0] ** 2 + k[1] ** 2)) for k, v in flux_dot.items()}
    alpha = kappa / n0  # choose G=1, enforce G*kappa=n0*alpha exactly.
    N_dot = scale(bracket(A, L), alpha)
    I = mean_product(N, bracket(A, L))
    expected_I = density_amplitude * a * b * m * n * (m * m - n * n) / 4
    assert I == expected_I
    assert bracket(potential, N) == {}
    assert mean_product(L, bracket(L, N)) == 0
    U = -mean_product(A, L) / 2
    Ke = de2 * mean_product(L, L) / 2
    Ki = n0 * Ti * mean_product(N, N) / 2
    Yhalf = n0 * Te * mean_product(N, N) / 2
    U_dot = -mean_product(L, A_dot)
    Ke_dot = de2 * mean_product(L, laplacian(A_dot))
    Ki_dot = n0 * Ti * mean_product(N, N_dot)
    Yhalf_dot = n0 * Te * mean_product(N, N_dot)
    assert U_dot + Ke_dot == -kappa * (Te + Ti) * I
    assert Ki_dot == n0 * Ti * alpha * I
    assert Yhalf_dot == n0 * Te * alpha * I
    proper_dot = U_dot + Ke_dot + Ki_dot + Yhalf_dot
    printed_density_dot = U_dot + Ke_dot + Ki_dot + 2 * Yhalf_dot
    isolated_main_sign_dot = U_dot + Ke_dot - Ki_dot - Yhalf_dot
    assert proper_dot == 0
    assert printed_density_dot == n0 * Te * alpha * I
    assert isolated_main_sign_dot == -2 * n0 * alpha * (Te + Ti) * I
    inertial_advection = scale(bracket(L, N), kappa * Ti * de2)
    return {
        'm': m, 'n': n, 'A_x_amplitude': a, 'A_y_amplitude': b,
        'N_amplitude': density_amplitude, 'Te': Te, 'Ti': Ti, 'de_squared': de2,
        'n0': n0, 'kappa': kappa, 'G': F(1), 'alpha': alpha, 'I': I,
        'U': U, 'Ke': Ke, 'Ki': Ki, 'Y_half': Yhalf,
        'U_dot': U_dot, 'Ke_dot': Ke_dot, 'Ki_dot': Ki_dot, 'Y_half_dot': Yhalf_dot,
        'consistent_total_dot': proper_dot,
        'printed_double_density_total_dot': printed_density_dot,
        'isolated_main_continuity_sign_total_dot': isolated_main_sign_dot,
        'inertial_advection_Fdot_squared_norm': mean_product(inertial_advection, inertial_advection),
        'ion_to_printed_density_ratio': Ti / (2 * Te),
        'ion_to_consistent_density_ratio': Ti / Te,
    }


def linear_case(Gamma0, Te, Ti, de2, kperp2, kpar2, me):
    # Use a real spatial phase pair A=a(t)cos(kz), N=n(t)sin(kz).
    # Restored induction coefficient gives a_dot=b*n with b>0;
    # literal main continuity gives n_dot=+a*a(t), consistent sign gives minus.
    omega2 = kpar2 * de2 * kperp2 * (Te + Ti / (1 - Gamma0)) / (me * (1 + de2 * kperp2))
    assert omega2 > 0
    return {'Gamma0_symbol': Gamma0, 'Te': Te, 'Ti': Ti, 'de_squared': de2,
            'kperp_squared': kperp2, 'kparallel_squared': kpar2, 'me': me,
            'consistent_omega_squared': omega2,
            'literal_main_lambda_squared': omega2,
            'consistent_lambda_squared': -omega2,
            'pressure_coefficient_restored_before_sign_isolation': True}


def poly_add(p, q):
    n = max(len(p), len(q))
    out = [F(0)] * n
    for i in range(n):
        out[i] = (p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, pi in enumerate(p):
        for j, qj in enumerate(q):
            out[i + j] += pi * qj
    return out


def gaussian_moment(power):
    if power % 2:
        return F(0)
    numerator = 1
    for odd in range(1, power, 2):
        numerator *= odd
    return F(numerator, 2 ** (power // 2))


def gaussian_average(poly):
    return sum((c * gaussian_moment(i) for i, c in enumerate(poly)), F(0))


def hermite_controls():
    H = [[F(1)], [F(0), F(2)]]
    for m in range(1, 8):
        H.append(poly_add([F(0)] + [2 * c for c in H[m]], [-2 * m * c for c in H[m - 1]]))
    orthogonality = []
    for m in range(9):
        for n in range(9):
            actual = gaussian_average(poly_mul(H[m], H[n]))
            expected = F(2 ** m * factorial(m)) if m == n else F(0)
            assert actual == expected
            orthogonality.append({'m': m, 'n': n, 'value': actual})
    source = [F(1), F(0), F(-2)]
    projections = []
    for m in range(9):
        numerator = gaussian_average(poly_mul(H[m], source))
        assert numerator == (F(-4) if m == 2 else F(0))
        projections.append({'m': m, 'unnormalized_projection': numerator,
                            'normalization_squared': F(2 ** m * factorial(m))})
    streaming = []
    for m in range(2, 8):
        # Projection of z H_(m+1), evaluated from exact Gaussian moments.
        numerator = gaussian_average(poly_mul(H[m], [F(0)] + H[m + 1]))
        squared = numerator ** 2 / (2 ** m * factorial(m) * 2 ** (m + 1) * factorial(m + 1))
        assert numerator > 0 and squared == F(m + 1, 2)
        streaming.append({'m': m, 'neighbor': m + 1,
                          'normalized_coefficient_squared': squared,
                          'Eq9_RHS_streaming_sign': -1, 'printed_Eq11_RHS_streaming_sign': 1})
    return {'Gaussian': 'exp(-z^2)/sqrt(pi)', 'physicists_Hermite_coefficients': H,
            'orthogonality_checks': orthogonality, 'drive_projections': projections,
            'g2_drive_in_units_sqrt2': F(-1), 'printed_Eq11_g2_drive_in_units_sqrt2': F(1),
            'streaming_pairs': streaming, 'collision_operator': 'set identically zero; convention not assessed'}


def dimensional_controls():
    # Gaussian-unit dimensions in independent bases (magnetic field, length, time).
    A_dot = (1, 1, -1)
    bare_gradient_N = (0, -1, 0)
    missing_cTe_over_e = (1, 2, -1)
    restored = tuple(a + b for a, b in zip(bare_gradient_N, missing_cTe_over_e))
    assert restored == A_dot and bare_gradient_N != A_dot
    return {'basis': ['magnetic_field', 'length', 'time'], 'A_time_derivative': A_dot,
            'c_parallel_potential_gradient': A_dot, 'bare_parallel_density_gradient': bare_gradient_N,
            'missing_cTe_over_e': missing_cTe_over_e, 'restored_density_term': restored,
            'context': 'Dimensional main Eq2 versus Appendix A2; not a secretly inferred simulation normalization.'}


def rate_controls():
    rows = []
    for i in range(1, 9):
        # Coherent rational nondimensional constants: 4*pi=1 is an absorbed unit
        # coefficient, NOT a numerical assertion about pi in Gaussian units.
        c, e, me, mi = F(1), F(1), F(1, i + 2), F(i + 1)
        n0, B0, B, R = F(1 + (i % 2)), F(i + 3), F(1, i + 1), F(i + 2)
        Ti, Te = F(i + 1, 2), F(i + 2, 3)
        de2 = me * c ** 2 / (n0 * e ** 2)
        di2 = mi * c ** 2 / (n0 * e ** 2)
        rhos2 = Te * mi * c ** 2 / (e ** 2 * B0 ** 2)
        VA2 = B ** 2 / (n0 * mi)
        tau2 = me * B0 ** 2 * R ** 2 / ((Te + Ti) * B ** 2)
        rec_tau2 = R ** 2 * tau2 / de2
        rate2 = R ** 2 / (VA2 * rec_tau2)
        source_rate2 = (1 + Ti / Te) * rhos2 / R ** 2
        assert rate2 == source_rate2
        outflow2 = (1 + Ti / Te) * rhos2 * VA2 / de2
        outflow_rate2 = R ** 2 / (outflow2 * rec_tau2)
        assert outflow_rate2 == de2 / R ** 2
        beta_i = 2 * n0 * Ti / B0 ** 2
        thermal = 1 + Te / Ti  # Z=1, tau=Ti/Te in the supplied supplement.
        response = 2 + beta_i * thermal
        ermhd_tau2 = response * me * B0 ** 2 * R ** 2 / (2 * Ti * thermal * B ** 2)
        ermhd_rec_tau2 = R ** 2 * ermhd_tau2 / de2
        ermhd_rate2 = R ** 2 / (VA2 * ermhd_rec_tau2)
        assert ermhd_rate2 == beta_i * thermal / response * di2 / R ** 2
        assert ermhd_rate2 / rate2 == 2 / response
        rows.append({'case': i, 'Te': Te, 'Ti': Ti, 'me': me, 'mi': mi, 'n0': n0,
                     'B0': B0, 'Bperp': B, 'R': R, 'de_squared': de2,
                     'rhos_squared': rhos2, 'tau_squared': tau2, 'reconnection_tau_squared': rec_tau2,
                     'main_Eq4_rate_squared': rate2, 'main_Eq5_rate_squared': outflow_rate2,
                     'supplement_Eq3_rate_squared': ermhd_rate2, 'beta_i': beta_i,
                     'ERMHD_to_lowbeta_squared_rate_ratio': 2 / response})
    return rows


def exponent_controls():
    rows = []
    for label, s in [('electron_only', F(2)), ('constant_rate_MHD', F(1))]:
        # Merger lifetime ~ R^s/B, and conserved flux RB is a phenomenological assumption.
        decay_power = (s + 3) / 2
        energy_t = -1 / (decay_power - 1)
        radius_t = -energy_t / 2
        assert energy_t == -2 / (s + 1)
        rows.append({'regime': label, 'lifetime_R_power_at_fixed_B': s,
                     'decay_ODE_energy_power': decay_power, 'energy_time_power': energy_t,
                     'radius_time_power': radius_t, 'field_time_power': -radius_t,
                     'wavenumber_time_power': -radius_t,
                     'critical_balance_length_time_power': 2 * radius_t if label == 'electron_only' else None})
    assert rows[0]['energy_time_power'] == F(-2, 3)
    assert rows[0]['critical_balance_length_time_power'] == F(2, 3)
    assert rows[1]['energy_time_power'] == -1
    return rows


def encode(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(v) for v in value]
    return value


def write_json(path, value):
    path.write_text(json.dumps(encode(value), indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')


def write_csv(path, rows):
    with path.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(encode(rows))


def figures(energy_rows):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12,
                         'axes.labelsize': 12, 'axes.titlesize': 12,
                         'xtick.labelsize': 11, 'ytick.labelsize': 11,
                         'legend.fontsize': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.dpi': 180,
                         'savefig.dpi': 180})
    metadata = {'Title': TITLE, 'Author': 'Taylor Kalin',
                'Description': 'Synthetic exact-equation controls; no source simulation data.'}
    blue, orange, green, red = '#246393', '#d58b23', '#26754d', '#ab3d44'
    row = next(r for r in energy_rows if r['m'] == 1 and r['n'] == 2 and
               r['Te'] == r['Ti'] == 1 and r['de_squared'] == F(1, 4))
    fig, ax = plt.subplots(1, 2, figsize=(11.8, 4.6), constrained_layout=True)
    x = np.arange(5)
    vals = [row['U_dot'], row['Ke_dot'], row['Ki_dot'], row['Y_half_dot'], F(0)]
    delta = [F(0), F(0), F(0), row['Y_half_dot'], row['printed_double_density_total_dot']]
    ax[0].bar(x - .17, list(map(float, vals)), .32, color=blue, label='Consistent half-density term')
    ax[0].bar(x + .17, [float(v + d) for v, d in zip(vals, delta)], .32, color=orange,
              label='Printed doubled density term')
    ax[0].axhline(0, color='#333333', linewidth=.9)
    ax[0].set_xticks(x, [r'$\dot U$', r'$\dot K_e$', r'$\dot K_i$', r'$\dot Y$', r'$\dot W$'])
    ax[0].set_ylabel('Instantaneous normalized energy derivative')
    ax[0].set_title('(a) Exact periodic state; full inertia retained', loc='left')
    ax[0].legend(loc='upper right')
    ax[0].text(.02, .04, r'$A=\cos x+\cos2y$, $N=\sin x\sin2y$' + '\n' +
               r'$T_e=T_i=1$, $d_e^2=1/4$', transform=ax[0].transAxes, fontsize=11)
    t = np.linspace(0, 2.5, 251)
    ax[1].plot(t, np.cosh(t), color=orange, linewidth=2.3, label='Literal main continuity sign')
    ax[1].plot(t, np.cos(t), color=green, linewidth=2.3, label='Appendix-consistent sign')
    ax[1].axhline(0, color='#333333', linewidth=.9)
    ax[1].set(xlabel=r'Dimensionless time $\tau=\Omega t$', ylabel=r'Illustrative mode amplitude $A/A(0)$')
    ax[1].set_title('(b) Linear sign control after restoring units', loc='left')
    ax[1].legend(loc='upper left')
    ax[1].text(.03, .035, 'Synthetic mode, not a source run',
               transform=ax[1].transAxes, fontsize=11)
    fig.savefig(ROOT / 'figures' / 'energy-and-wave-controls.png', metadata=metadata)
    plt.close(fig)
    fig, ax = plt.subplots(1, 2, figsize=(11.8, 4.5), constrained_layout=True)
    z = np.linspace(-3.5, 3.5, 501)
    F0 = np.exp(-z * z) / np.sqrt(np.pi)
    psi2 = (4 * z * z - 2) / np.sqrt(8)
    source = (1 - 2 * z * z) * F0
    ax[0].plot(z, source, color=blue, linewidth=2.7, label=r'Eq. (9): $(1-2z^2)F_0$')
    ax[0].plot(z, -np.sqrt(2) * psi2 * F0, color=green, linestyle='--', linewidth=1.9,
               label=r'Exact projection: $-\sqrt{2}\,\psi_2 F_0$')
    ax[0].plot(z, np.sqrt(2) * psi2 * F0, color=orange, linestyle=':', linewidth=2.3,
               label=r'Eq. (11) drive: $+\sqrt{2}\,\psi_2 F_0$')
    ax[0].axhline(0, color='#333333', linewidth=.9)
    ax[0].set(xlabel=r'$z=v_\parallel/v_{\mathrm{the}}$', ylabel='Velocity dependence per unit spatial drive')
    ax[0].set_ylim(-1.05, .7)
    ax[0].set_title('(a) Stated Gaussian and Hermite convention', loc='left')
    ax[0].legend(loc='lower center')
    ax[1].bar([-.18, .82], [-1, -1], width=.32, color=blue, label='Directly projected Eq. (9)')
    ax[1].bar([.18, 1.18], [1, 1], width=.32, color=orange, label='Printed Eq. (11)')
    ax[1].axhline(0, color='#333333', linewidth=.9)
    ax[1].set_xticks([0, 1], [r'$g_2$ drive / $\sqrt{2}$', r'$g_2\leftarrow g_3$ / $\sqrt{3/2}$'])
    ax[1].set(ylim=(-1.6, 1.8), ylabel='Signed coefficient after moving streaming to RHS')
    ax[1].set_yticks([-1, 0, 1])
    ax[1].set_title('(b) Two collisionless coefficient checks', loc='left')
    ax[1].legend(loc='upper center')
    ax[1].text(.5, .04, 'Collisions set to zero; no heating simulation', ha='center',
               transform=ax[1].transAxes, fontsize=11)
    fig.savefig(ROOT / 'figures' / 'hermite-projection-controls.png', metadata=metadata)
    plt.close(fig)


def main():
    if not __debug__:
        raise RuntimeError('Do not run with -O: exact scientific assertions must remain enabled.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--no-plots', action='store_true', help='Run all exact controls using only the standard library.')
    args = parser.parse_args()
    for folder in ('data', 'figures'):
        (ROOT / folder).mkdir(exist_ok=True)
    patterns = [(1, 2, F(1), F(1), F(1)), (2, 3, F(1, 2), F(2), F(-1)),
                (3, 1, F(2), F(1, 3), F(3, 2)), (1, 1, F(1), F(1), F(1)),
                (1, 2, F(0), F(1), F(1))]
    energy = []
    for j, (m, n, a, b, density_amplitude) in enumerate(patterns):
        for Te, Ti in [(F(1), F(1)), (F(1, 2), F(2)), (F(3), F(1, 3)), (F(2), F(3))]:
            for de2 in (F(0), F(1, 4), F(2)):
                row = energy_case(m, n, a, b, density_amplitude, Te, Ti, de2, F(1 + j % 2), F(1, 1 + j % 2))
                row['case'] = len(energy) + 1
                energy.append(row)
    linear = [linear_case(g, Te, Ti, d, k, F(1, 4), F(1, 2))
              for g in (F(0), F(1, 4), F(3, 4))
              for Te, Ti in ((F(1), F(1)), (F(2), F(1, 3)))
              for d in (F(1, 4), F(2)) for k in (F(1), F(5))]
    hermite = hermite_controls()
    rates = rate_controls()
    powers = exponent_controls()
    assert len(energy) == 60 and len(linear) == 24
    nonzero = sum(r['I'] != 0 for r in energy)
    assert nonzero == 36
    assert all(r['printed_double_density_total_dot'] != 0 for r in energy if r['I'] != 0)
    assert any(r['inertial_advection_Fdot_squared_norm'] > 0 for r in energy)
    report = {
        'title': TITLE, 'author': 'Taylor Kalin', 'status': 'all exact controls passed',
        'producer_sha256': sha(Path(__file__).read_bytes()), 'source': SOURCE,
        'scope': 'Printed-equation consistency of named editions; synthetic instantaneous states, linear symbols and standard Gaussian identities only. No original source simulation or final VOR was reproduced.',
        'counts': {'periodic_energy_states': len(energy), 'nonzero_exchange_states': nonzero,
                   'zero_exchange_controls': len(energy) - nonzero, 'linear_symbol_states': len(linear),
                   'Hermite_orthogonality_pairs': 81, 'Hermite_drive_projections': 9,
                   'Hermite_neighbor_streaming_pairs': 6, 'rate_parameter_states': len(rates),
                   'conditional_decay_regimes': len(powers)},
        'normalization': {'energy': 'G=1, alpha=kappa/n0, hence G*kappa=n0*alpha; rational nondimensional examples, not dimensional parameter inference.',
                          'rate': 'A coherent rational normalization absorbs 4*pi into units; Gaussian dimensional reasoning is checked separately.',
                          'Fourier': 'Exact full finite convolution, no truncation/dealiasing; mean is zero Fourier coefficient on [0,2pi]^2.',
                          'inertia': 'All de^2 Laplacian terms and full generalized-flux advection retained for energy tests; de^2=0 is only a mathematical limiting control.'},
        'energy': energy, 'linear': linear, 'dimensional': dimensional_controls(), 'hermite': hermite,
        'retained_rate_controls': rates, 'retained_conditional_exponents': powers,
        'limits': ['AM is distinct from the uninspected subscription VOR.',
                   'Supplement identities refer only to arXiv v2; final journal supplement not inspected.',
                   'No author implementation, raw diagnostics, reconnection curve or heating calculation is inferred.',
                   'Rate and decay checks retain the source assumptions and suppress order-one sheet prefactors.',
                   'The source explicitly labels its ideal-ERMHD flux-breaking extension hypothetical.',
                   'No quantitative reanalysis of the published energy/equipartition plots is possible from these controls.'],
    }
    write_json(ROOT / 'data' / 'equation-controls.json', report)
    write_csv(ROOT / 'data' / 'periodic-energy-controls.csv', energy)
    write_csv(ROOT / 'data' / 'linear-symbol-controls.csv', linear)
    write_csv(ROOT / 'data' / 'retained-rate-controls.csv', rates)
    write_csv(ROOT / 'data' / 'conditional-exponents.csv', powers)
    if not args.no_plots:
        figures(energy)
    print(json.dumps({'status': report['status'], 'counts': report['counts'], 'figures_generated': not args.no_plots}))


if __name__ == '__main__':
    main()
