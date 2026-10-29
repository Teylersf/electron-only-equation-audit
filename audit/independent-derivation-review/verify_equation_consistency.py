"""Original exact local controls; no source code, other verifier or simulation import.

Gaussian-rational Fourier coefficients make the periodic energy witness exact.
Normalized constants in that witness absorb common dimensional coefficients.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import itertools
import json
import platform
import sys


ZERO = (F(0), F(0))


def zadd(a, b):
    return a[0]+b[0], a[1]+b[1]


def zmul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def clean(a):
    return {k:v for k,v in a.items() if v != ZERO}


def plus(*fields):
    out = {}
    for field in fields:
        for k, v in field.items():
            out[k] = zadd(out.get(k, ZERO), v)
    return clean(out)


def times(a, b):
    out = {}
    for (i,j), u in a.items():
        for (k,l), v in b.items():
            key = (i+k,j+l)
            out[key] = zadd(out.get(key, ZERO), zmul(u,v))
    return clean(out)


def scale(a, q):
    return clean({k:(v[0]*q,v[1]*q) for k,v in a.items()})


def diff(a, axis):
    return clean({k:zmul(v,(F(0),F(k[axis]))) for k,v in a.items()})


def lap(a):
    return plus(diff(diff(a,0),0),diff(diff(a,1),1))


def bracket(a,b):
    return plus(times(diff(a,0),diff(b,1)),scale(times(diff(a,1),diff(b,0)),-1))


def average(a):
    real, imag = a.get((0,0),ZERO)
    assert imag == 0
    return real


def cosine(k,l):
    return {(k,l):(F(1,2),F(0)),(-k,-l):(F(1,2),F(0))}


def sine(k,l):
    return {(k,l):(F(0),-F(1,2)),(-k,-l):(F(0),F(1,2))}


def gaussian_moment(power):
    if power % 2:
        return F(0)
    value = F(1)
    for j in range(1,power//2+1):
        value *= F(2*j-1,2)
    return value


def poly_product(a,b):
    result = {}
    for i,u in a.items():
        for j,v in b.items():
            result[i+j] = result.get(i+j,F(0))+u*v
    return result


def mean_poly(a):
    return sum((coefficient*gaussian_moment(power)
                for power,coefficient in a.items()),F(0))


def encode(value):
    if isinstance(value,F):
        return str(value)
    if isinstance(value,dict):
        return {str(k):encode(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):
        return [encode(x) for x in value]
    return value


def main():
    if sys.flags.optimize:
        raise RuntimeError("Use ordinary Python without -O; exact guards must remain enabled.")
    A = plus(cosine(1,0),cosine(0,2))
    N = times(sine(1,0),sine(0,2))
    density_drive = bracket(A,lap(A))
    assert average(times(N,density_drive)) == -F(3,2)
    assert bracket(scale(A,-1),lap(scale(A,-1))) == density_drive
    energy = []
    for Ti,Te,de2 in itertools.product([F(1),F(2)],[F(1),F(3)],[F(1,16),F(1,4)]):
        phi = scale(N,-Ti)  # strict subion Boltzmann closure
        Astar = plus(A,scale(lap(A),-de2))
        Nt = plus(density_drive,scale(bracket(phi,N),-1))
        Astar_t = plus(scale(bracket(phi,Astar),-1),scale(bracket(A,N),-Te))
        magnetic = -average(times(lap(A),Astar_t))
        ion = -average(times(phi,Nt))
        electron_half = Te*average(times(N,Nt))
        assert magnetic+ion+electron_half == 0
        printed = magnetic+ion+2*electron_half
        assert printed == -F(3,2)*Te and printed != 0
        energy.append({"Ti":Ti,"Te":Te,"de_squared":de2,
                       "magnetic_derivative":magnetic,"ion_derivative":ion,
                       "half_density_derivative":electron_half,
                       "corrected_W_derivative":F(0),"printed_double_density_W_derivative":printed,
                       "printed_Ki_over_Y":Ti/(2*Te),"half_density_Ki_over_Y":Ti/Te})

    H2 = {2:F(4),0:F(-2)}
    H3 = {3:F(8),1:F(-12)}
    source = {0:F(1),2:F(-2)}
    drive_projection = mean_poly(poly_product(H2,source))
    norm2 = mean_poly(poly_product(H2,H2))
    streaming_projection = mean_poly(poly_product(poly_product(H2,{1:F(1)}),H3))
    assert drive_projection == -4 and norm2 == 8 and streaming_projection == 24

    linear = []
    for Gamma in [F(0),F(1,4),F(3,4)]:
        e,c,me,de2,Te,Ti,kz,kp2 = F(1),F(1),F(5),F(1,4),F(2),F(3),F(3),F(4)
        a = kz*e*de2*kp2/(c*me)
        b = kz*c*(Te+Ti/(1-Gamma))/(e*(1+de2*kp2))
        assert a*b > 0
        linear.append({"Gamma":Gamma,"printed_continuity_time_eigenvalue_squared":a*b,
                       "repaired_continuity_time_eigenvalue_squared":-a*b,
                       "repaired_wave_frequency_squared":a*b,
                       "scope":"Pressure coefficient restored first, to isolate the continuity-sign consequence."})

    rates = []
    for Te,Ti,me in itertools.product([F(1),F(3)],[F(1),F(2)],[F(1,100),F(1,10)]):
        c,e,mi,mu,Bg,Bp,R = F(2),F(1),F(1),F(5),F(3),F(1),F(1,2)
        de2 = me*c*c/(mu*e*e)  # mu=4*pi*n
        rhos2 = Te*mi*c*c/(e*e*Bg*Bg)
        vai2 = Bp*Bp/(mu*mi)
        tau_balance2 = me*Bg*Bg*R*R/((Te+Ti)*Bp*Bp)
        tau_source2 = R*R*de2/((1+Ti/Te)*rhos2*vai2)
        assert tau_balance2 == tau_source2
        taurec2 = tau_balance2*R*R/de2
        rate2 = R*R/(taurec2*vai2)
        assert rate2 == (1+Ti/Te)*rhos2/(R*R)
        outflow2 = R**4/(de2*taurec2)
        assert R*R/(taurec2*outflow2) == de2/(R*R)
        beta_i = 2*mu*Ti/(Bg*Bg)
        g = 1+Te/Ti
        di2 = mi*c*c/(mu*e*e)
        assert beta_i*g*di2/(2*R*R) == rate2  # leading low-beta ERMHD limit
        zeta = 2+beta_i*g
        er_tau2 = zeta*Bg*Bg*me*R**4/(2*de2*Ti*g*Bp*Bp)
        assert R*R/(er_tau2*vai2) == beta_i*g*di2/(zeta*R*R)
        rates.append({"Te":Te,"Ti":Ti,"me":me,"tau_squared":tau_balance2,
                      "rate_squared":rate2,"ERMHD_balance_squared_rate":beta_i*g*di2/(zeta*R*R),
                      "low_beta_matching_pass":True,"outflow_normalization_pass":True})

    # Dimensions are ordered (mass,length,time), in Gaussian mechanical units.
    dimensions = {
        "A_time_derivative":[F(1,2),F(1,2),F(-2)],
        "printed_density_gradient":[F(0),F(-1),F(0)],
        "c_Te_over_e_times_density_gradient":[F(1,2),F(1,2),F(-2)],
        "printed_four_pi_n_m_over_B_squared":[F(0),F(-2),F(2)],
        "usual_eight_pi_n_T_over_B_squared":[F(0),F(0),F(0)],
    }
    assert dimensions["A_time_derivative"] != dimensions["printed_density_gradient"]
    assert dimensions["A_time_derivative"] == dimensions["c_Te_over_e_times_density_gradient"]
    result = {
        "schema_version":1,"status":"pass","environment":{"python":platform.python_version(),"standard_library_only":True},
        "program_SHA256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope":"Original local equation-consistency and positive scaling controls, not a source-simulation, eigenproblem or nonlinear plasma reproduction.",
        "source_scope":{"arxiv":"2407.06020v2","supplied_PDF_SHA256":"e482988aa241494c52cc6071317fbd6f3a1c084173f045f2bfc03ba0ade26cd8",
                        "AM_main_PDF_SHA256":"71c9216d20334427fdc84570c72b600c82c7009721f03837787f8d5a74eadd83",
                        "VOR_or_journal_supplement_identity_verified":False},
        "dimensions":dimensions,
        "two_dimensional_sign_control":{"average_N_times_bracket_A_lapA":-F(3,2),
                                        "main_2D_continuity_vs_Appendix_signs_opposite":True,
                                        "A_sign_reversal_leaves_quadratic_bracket_unchanged":True},
        "linear_wave_controls":linear,"periodic_energy_controls":energy,
        "Hermite_projection":{"Gaussian_weight":"exp(-z^2)/sqrt(pi)","H2":"4z^2-2","H3":"8z^3-12z",
                              "unnormalized_H2_drive_projection":drive_projection,"H2_norm_squared":norm2,
                              "normalized_g2_drive":"-sqrt(2)","printed_g2_drive":"+sqrt(2)",
                              "H2_z_H3_projection":streaming_projection,
                              "normalized_m2_streaming_coupling":"sqrt(3/2); it moves to the RHS with a minus sign for the stated Eq9."},
        "positive_reconnection_and_ERMHD_controls":rates,
        "decay_scaling_positive_control":{"subion":"tau_rec proportional to R^2/B; conserved R*B gives dE/dt proportional to -E^(5/2), hence E proportional to t^(-2/3).",
                                         "MHD":"constant ion-Alfven normalized rate and conserved R*B give tau proportional to B^(-2), hence E proportional to t^(-1).",
                                         "parallel_scale":"Critical balance under fixed model coefficients gives l proportional to R/B, hence t^(2/3) in the adopted subion decay."},
        "limits":["AM checks here cover the main equations/Appendix only; no AM supplement or subscription VOR was represented as read.",
                  "Changing density-energy coefficient or continuity signs is a repair of printed expressions, not evidence that source code or plotted diagnostics used those expressions.",
                  "The ERMHD rate is checked as the source's explicitly hypothetical term balance, not a justified flux-breaking model.",
                  "Ion-entropy operator is interpreted as its standard self-adjoint quadratic form, not as an operator on the entire squared field.",
                  "All exact local witnesses are independent of original simulation data; no numerical plasma results are rejected."]
    }
    target = Path(__file__).with_name("equation-consistency-checks.json")
    target.write_text(json.dumps(encode(result),ensure_ascii=False,indent=2,allow_nan=False)+"\n",encoding="utf-8")
    print(json.dumps({"status":"pass","energy_witnesses":len(energy),"linear_wave_cases":len(linear),
                      "positive_rate_cases":len(rates),"Hermite_drive_projection":str(drive_projection),
                      "program_SHA256":result["program_SHA256"],
                      "receipt_SHA256":hashlib.sha256(target.read_bytes()).hexdigest()}))


if __name__ == "__main__":
    main()
