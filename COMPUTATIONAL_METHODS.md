# Computational methods and evidence limits

## Editions and locators

The supplied 19-page PDF is byte-identical to arXiv:2407.06020v2. Its main article occupies pages 1–9; the embedded ten-page supplement occupies pages 10–19. The independently acquired authentic CHORUS accepted manuscript has a cover and nine printed manuscript pages; it is not the subscription version of record (VOR). All 19 supplied pages, all ten accepted-manuscript pages and the complete v2 main TeX were read before writing this producer. The critical displays were also inspected visually.

The relevant source expressions are main Eqs. (1)–(3), Appendix (A1)–(A4), and supplemental Eqs. (7)–(12). Main Eqs. (1)–(2) and Appendix (A1)–(A2) occur on supplied pages 1 and 5, or accepted-manuscript PDF pages 2 and 6 (printed pages 1 and 5). Supplemental Eqs. (9) and (11) are on combined page 15 (supplement p. 6); Eq. (12) is on combined page 17 (supplement p. 8). Supplementary claims are not comparisons with an independently obtained final journal supplement.

## Exact finite Fourier controls

The original producer represents finite periodic fields by real rational coefficients of `exp(i(kx*x+ky*y))`. Products use complete finite convolution, without truncation. A Poisson bracket multiplies each pair of coefficients by `-(px*qy-py*qx)`, because the two derivatives supply `i*i=-1`. The spatial mean is the zero Fourier coefficient. The selected fields have real coefficients and obey the required inversion symmetry.

The family is

\[
A=a\cos(mx)+b\cos(ny),\qquad N=h\sin(mx)\sin(ny),\qquad N=\delta n_e/n_0.
\]

The exact convolution is checked independently against

\[
I=\langle N\{A,\Delta A\}\rangle
=\frac{habmn(m^2-n^2)}4.
\]

Five field patterns, four positive temperature pairs and three inertia values produce 60 states. The patterns `(m,n,a,b,h)` are `(1,2,1,1,1)`, `(2,3,1/2,2,-1)`, `(3,1,2,1/3,3/2)`, `(1,1,1,1,1)`, and `(1,2,0,1,1)`. The last two supply zero-exchange controls. Temperature pairs `(Te,Ti)` are `(1,1)`, `(1/2,2)`, `(3,1/3)`, `(2,3)`; `de^2` is `0`, `1/4` or `2`. The zero-inertia case is only a limiting mathematical control; the source reconnection calculation assumes finite inertia.

With strict-subion closure, let `varphi=e*phi_physical` denote the energy-normalized potential (the rational examples set `e=1`). Define

\[
F=A-d_e^2\Delta A,\quad \varphi=-T_iN,\quad
\partial_tN=\alpha\{A,\Delta A\},
\]

\[
\partial_tF=-\kappa\{\varphi,F\}-\kappa T_e\{A,N\},
\qquad G\kappa=n_0\alpha.
\]

The examples choose `G=1` and positive rational `n0,kappa`, enforcing this relation exactly. In dimensional Gaussian notation the corresponding factors are `G=1/(4*pi)`, `kappa=c/(e*B0)` and `alpha=e*de^2/(B0*c*me)`; the relation follows from the definition of `de`. Rational examples are coherent nondimensionalizations, not numerical replacements of physical pi. The full inertial-advection term `kappa*Ti*de^2*{Delta A,N}` is retained. The exact inversion of `1-de^2*Delta` is performed mode by mode.

The ledger is

\[
U=\frac G2\langle|\nabla A|^2\rangle,\quad
K_e=\frac{Gd_e^2}2\langle(\Delta A)^2\rangle,\quad
K_i=\frac{n_0T_i}2\langle N^2\rangle,\quad
Y_{1/2}=\frac{n_0T_e}2\langle N^2\rangle.
\]

Direct field derivatives, not a prescribed cancellation, give

\[
\dot U+\dot K_e=-G\kappa(T_e+T_i)I,
\quad \dot K_i=n_0T_i\alpha I,
\quad \dot Y_{1/2}=n_0T_e\alpha I.
\]

Thus the consistent total derivative vanishes exactly. Replacing only the density term with the doubled term printed in supplemental Eq. (12) leaves `n0*Te*alpha*I`; all 36 nonzero-exchange controls have nonzero residual. Reversing only the density-evolution sign, after restoring the pressure coefficient and leaving the same half-density energy, leaves `-2*n0*alpha*(Te+Ti)*I`. This isolates a display inconsistency; it is not an implemented-source-model claim. The program also verifies `mean(Delta A*{Delta A,N})=0`, while confirming that the retained inertial-advection field itself need not vanish.

For the figure's root witness, `A=cos(x)+cos(2y)`, `N=sin(x)*sin(2y)`, `Te=Ti=1`, `de^2=1/4`, `n0=kappa=G=alpha=1`, `I=-3/2`. The individual derivatives are `Udot=21/20`, `Kedot=39/20`, `Kidot=Yhalf_dot=-3/2`; the consistent sum is zero and the doubled-density sum is `-3/2`. These are instantaneous derivatives of an admissible periodic state, not a numerical time integration.

## Main-system dimensional and linear controls

With its stated `b.grad=partial_z-{A,...}/B0`, positive main Eq. (1) reduces to a negative two-dimensional bracket, whereas Appendix (A1) prints a positive bracket. The continuity bracket is quadratic in `A`; changing the sign of `A` alone cannot remove that discrepancy. Main Eq. (2)'s bare density gradient lacks the `c*Te/e` coefficient carried by Appendix (A2). A Gaussian-unit dimension-vector check keeps these issues separate from a possible declared normalization.

For the linear sign test, first restore that pressure coefficient. Poisson closure for a perpendicular Fourier symbol `0<=Gamma0<1` gives `phi=-Ti*N/[e*(1-Gamma0)]`. A real spatial phase pair `A=a(t)*cos(kparallel*z)`, `N=n(t)*sin(kparallel*z)` yields a positive induction coefficient and

\[
\Omega^2=\frac{k_\parallel^2d_e^2k_\perp^2}
 {m_e(1+d_e^2k_\perp^2)}
\left(T_e+\frac{T_i}{1-\Gamma_0}\right)>0.
\]

The literal main continuity sign gives `a''=+Omega^2*a`, while the Appendix-consistent sign gives `a''=-Omega^2*a`. Twenty-four rational symbol cases use `Gamma0=0,1/4,3/4`, two temperature pairs, two positive inertia values and two perpendicular squared wavenumbers. Figure 1(b) simply plots `cosh(tau)` and `cos(tau)` for initial amplitude 1 and initial derivative 0, with `tau=Omega*t`. It demonstrates the isolated sign effect, not an unstable source simulation.

## Collisionless Hermite projection

For normalized Gaussian `F0=exp(-z^2)/sqrt(pi)` and the stated physicists' Hermite basis `psi_m=H_m/sqrt(2^m*m!)`, the program constructs `H_0` through `H_8` from their polynomial recurrence. Exact Gaussian moments are `(2j-1)!!/2^j` for even powers and zero for odd powers. It verifies 81 orthogonality pairs and nine source projections. Since `H_2=4*z^2-2`,

\[
(1-2z^2)=-H_2/2=-\sqrt2\,\psi_2,
\quad \langle H_2(1-2z^2)\rangle=-4.
\]

Consequently supplemental Eq. (9) projects to a negative `sqrt(2)` drive, whereas printed Eq. (11) has a positive drive. The polynomial projection also checks six neighboring streaming magnitudes `sqrt((m+1)/2)`, from `m=2` through `7`. Moving the streaming term from Eq. (9)'s left side to the right gives a negative coefficient under the stated field-parallel convention; Eq. (11) prints a positive coefficient. The temperature subtraction only removes a lower Hermite moment and does not change these `m>=2` neighbor tests. Collisions are identically zero, avoiding an assumption about the separately written collision functional's sign convention. Figure 2 presents these Gaussian identities only.

## Retained physical scaling algebra

Eight rational parameter sets independently eliminate the Appendix sheet balances and retain main Eq. (4), `Rrec^2=(1+Ti/Te)*rhos^2/R^2`, and Eq. (5), `Rrec,e^2=de^2/R^2`. The same parameter sets retain the supplemental beta-order-unity rate with its **entire fraction inside the square root**. For charge state one, `beta_i=8*pi*n0*Ti/B0^2`, its squared-rate ratio to the low-beta result is `2/[2+beta_i*(1+Te/Ti)]`, approaching one in the common low-beta limit. The source explicitly calls its flux-breaking ERMHD extension hypothetical; the checks do not supply the missing microscopic reconnection closure.

Conserved merger flux `R*B`, volume filling and a merger-controlled lifetime are assumptions. Under those assumptions, `tau~R^2/B` yields the source's `E~t^(-2/3)`, `R~t^(1/3)`, `B~t^(-1/3)` and critical-balance `l~t^(2/3)`. Constant-rate MHD lifetime `tau~R/B` yields `E~t^(-1)` and `R~t^(1/2)`. These exact exponent controls are positive findings; they are not fitted source-data estimates. No inference about a published spectrum, raw energy trace, or actual GX diagnostic follows from this package.

The strongest benign interpretation remains recognizable printed transcription/normalization defects in an established model. Appendix A already carries the consistent core sign and coefficient. The source discloses finite scale separation, hyperdiffusion, isothermal limitations, volume-filling assumptions and the hypothetical beta-order-unity extension. Those qualifications remain in force. The present calculations neither establish a different reconnection mechanism nor overturn the published phenomenology.
