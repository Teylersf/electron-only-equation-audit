# Independent equation and scaling audit

Target: Liu, Silva, Milanese, Zhou, Mandell and Loureiro, arXiv:2407.06020v2, “Electron-only magnetic reconnection and inverse magnetic-energy transfer at sub-ion scales.” All nineteen supplied pages, including the ten-page supplement, were read. The v2 author TeX was consulted for the main equations and Appendix A. Selected main/Appendix equations were also inspected directly in the publisher-hosted accepted manuscript (AM).

The AM is not the subscription version of record (VOR). The supplied supplement is audited as the v2 supplement; no claim is made that its formulas were compared with a separately retrieved final journal supplement. Equation labels below distinguish main, Appendix and supplement numbering.

## Assessment

There are several reproducible inconsistencies in the printed governing expressions. They are more specific than a disagreement with a phenomenological assumption: direct reduction, dimensions, a Gaussian moment projection and an exact periodic free-energy derivative give incompatible results for expressions represented as the same model.

The strongest benign interpretation is transcription or normalization errors in the displays. Appendix A already supplies the pressure coefficient and a continuity sign consistent with stable kinetic-Alfvén dynamics. Its reconnection-time calculation, the normalized rate, the conditional coalescence exponents and the stated hypothetical order-unity-beta extension retain their algebraic support. Nothing here identifies the expressions actually advanced by GX or the diagnostics used to produce the figures.

## 1. Main pressure coefficient and two-dimensional sign

Main Eq. (2), supplied page 1 and AM printed page 1/PDF page 2, has a bare parallel derivative of \(N=\delta n_e/n_{0e}\). The v2 author TeX, lines 110–112, confirms the printed form. Appendix Eq. (A2), supplied page 5 and AM printed page 5/PDF page 6, instead contains \(cT_{0e}/e\) multiplying the corresponding density bracket. In the dimensional notation retained in the model, the consistent Ohm term is

\[
\frac{cT_{0e}}e\,\widehat{\boldsymbol b}\cdot\nabla N.
\]

A bare density gradient has dimensions of inverse length, whereas \(\partial_t A_z\) has the dimensions of vector potential divided by time. Multiplication by \(cT_{0e}/e\) supplies the missing dimensions. A normalization could set this coefficient numerically to one only if the relevant rescalings were declared consistently; that would not explain an unannounced difference between the main display and its stated Appendix rewrite.

Independently, main Eq. (1) has a positive field-parallel derivative of
\(u_{ze}=\alpha\nabla_\perp^2A_z\), \(\alpha=e d_e^2/(cm_e)>0\). The immediately stated definition is
\(\widehat{\boldsymbol b}\cdot\nabla=\partial_z-\{A_z,\cdot\}/B_z\).
For \(\partial_z=0\), direct substitution therefore gives a negative bracket. Appendix Eq. (A1) instead prints a positive bracket. This sign discrepancy is present in both inspected main/Appendix editions and the v2 TeX (main line 110; Appendix line 316).

Changing \(A_\parallel\) to \(-A_z\) cannot fix the discrepancy: the quadratic bracket obeys \(\{-A,\nabla^2(-A)\}=\{A,\nabla^2A\}\). A global orientation change also changes the other bracket and field definitions and is not the stated reduction.

A positive control isolates the continuity sign by first restoring the pressure coefficient. For a perpendicular Fourier mode with \(0\le\Gamma_0<1\), Poisson closure gives \(\varphi=-T_iN/[e(1-\Gamma_0)]\). The physically oscillatory sign yields

\[
\omega^2=
\frac{k_\parallel^2d_e^2k_\perp^2}
 {m_e(1+d_e^2k_\perp^2)}
\left(T_e+\frac{T_i}{1-\Gamma_0}\right)>0.
\]

The positive continuity sign printed in main Eq. (1) gives the negative of this frequency squared, or positive real time-growth eigenvalues. Appendix (A1)'s sign gives the oscillatory result. This is a consequence of reading the displays literally, not a report that the source simulations exhibited that growth.

## 2. Density energy in the supplied supplement

Supplement Eq. (12), supplied page 17/supplement page 8, prints
\(Y=n_0T_e\langle N^2\rangle\), without one half. Its ion-entropy term carries one half. Interpreting the ion operator in its usual self-adjoint quadratic-form sense, strict subion Poisson closure gives
\[
K_i=\frac{n_0T_i}{2}\langle N^2\rangle,
\qquad
\frac{K_i}{Y_{\rm printed}}=\frac{T_i}{2T_e}.
\]
Thus at \(T_i=T_e\), the definitions imply \(K_i/Y=1/2\), while the following text on supplied page 18 states approximately equal ion entropy and density energy and attributes that equality to the same closure.

The quadratic invariant of the consistent Appendix two-field system requires
\[
Y_{\rm consistent}=\frac{n_0T_e}{2}\langle N^2\rangle.
\]
With this coefficient, \(K_i/Y=T_i/T_e\), which agrees with the explanatory equality when the temperatures are equal.

This is also a conservation test, not merely a comparison with a familiar formula. An original periodic Fourier witness uses
\(A=\cos x+\cos2y\), \(N=\sin x\sin2y\), \(\varphi=-T_iN\), and the Appendix signs. After common positive dimensional factors are absorbed into normalization, \(\langle N\{A,\nabla^2A\}\rangle=-3/2\). The magnetic, ion-entropy and half-density derivatives sum exactly to zero; using the doubled printed density term gives \(dW/dt=-3T_e/2\ne0\). Eight positive-temperature/inertial-length variants pass exactly.

A global multiplication of the invariant cannot fix a coefficient mismatch in only one term. Nor is the density variance an independent invariant of a general coupled state, as the explicit witness demonstrates. However, the plot's near equality could mean the diagnostic already used the consistent half coefficient. No raw diagnostic arrays or exact implementation were inspected, so the figures and numerical energy evolution are not declared wrong.

## 3. Hermite projection

Supplement Eq. (9), supplied page 15/supplement page 6, has the drive
\((1-2z^2)F_0\,\widehat{\boldsymbol b}\cdot\nabla u_{ze}\),
where \(z=v_\parallel/v_{\rm the}\) and \(F_0\propto e^{-z^2}\).
The stated normalization \(H_m/\sqrt{2^m m!}\) fixes the usual physicists' Hermite basis. For \(H_2=4z^2-2\),
\[
\left\langle H_2(1-2z^2)\right\rangle_{F_0}=-4,
\qquad \langle H_2^2\rangle_{F_0}=8.
\]
The resulting \(g_2\) drive is \(-\sqrt2\,\widehat{\boldsymbol b}\cdot\nabla u_{ze}\), whereas supplement Eq. (11) prints \(+\sqrt2\). The streaming term also moves from Eq. (9)'s left side to Eq. (11)'s right side with a minus sign; the printed hierarchy instead has a plus sign. In particular, the normalized \(g_2\)-to-\(g_3\) coefficient has magnitude \(\sqrt{3/2}\).

The exact check sets collisions to zero. It does not assign a sign convention to the separately written collision functional. Reversing the velocity coordinate changes odd Hermite coefficients but leaves the \(m=2\) drive unchanged; redefining \(g_e\) globally would also change the explicitly printed distribution and temperature-moment definitions. These alternatives do not make the two stated equations identical without further changes.

## 4. Supplementary dimensional displays

The beta definition on supplied page 12/supplement page 3 is visibly \(4\pi n_{0i}m_i/B_z^2\), which has dimensions of inverse velocity squared in dimensional Gaussian notation. The conventional dimensionless ion beta is \(8\pi n_{0i}T_i/B_z^2\). An unstated thermal-speed unit could make the numerical expressions coincide, so the appropriate bounded claim is a missing dimensional/normalization declaration, not proof of a different implemented model. Using the conventional beta makes the supplement's rate reduction internally consistent.

Supplement Eq. (4), supplied page 14/supplement page 5, has a bare \(\partial_zN\) term after its nonlinear Ohm terms are combined. Starting from the coefficient-consistent induction equation and \(N=-e\varphi/T_i\), neglecting electron inertia gives
\[
\partial_tA=
\frac{c(T_e+T_i)}e\,\partial_zN
-\frac{c(T_e+T_i)}{eB_0}\{A,N\}.
\]
The displayed nonlinear coefficient agrees; the parallel term lacks its coefficient. This is a further printed-expression issue. It does not by itself invalidate the shell-to-shell nonlinear diagnostic or identify the equation implemented by a three-dimensional code.

## 5. Retained results, approximations and exclusions

The source's reconnection scaling survives direct elimination of its sheet balances. With \(\delta_x\sim d_e\), \(\delta_y\sim R\), \(A_{\rm sheet}\sim B_\perp d_e\), and the consistent Appendix coefficients,
\[
\tau^2\sim\frac{m_eB_z^2\delta_y^2}{(T_e+T_i)B_\perp^2},
\qquad
\tau_{\rm rec}\sim\frac{R}{d_e}\tau.
\]
These are equivalent to Appendix (A7)–(A8) and main Eq. (4):
\(\mathcal R_{\rm rec}\sim\sqrt{1+T_i/T_e}\,\rho_s/R\).
Normalization to the separately estimated outflow speed gives Eq. (5), \(d_e/R\); this is an outflow-time normalization, not an assertion that the speed equals the electron Alfvén speed with unit coefficient. Eight independently evaluated parameter sets retain these relations.

The beta-order-unity rate in supplement Eq. (3), page 13, has the entire fraction inside its square root. That grouping was inspected visually. With standard dimensionless ion beta it follows from the two displayed ERMHD balances and tends to the low-beta rate in their common limit. Crucially, the source explicitly states that ideal ERMHD lacks the flux-breaking physics needed for reconnection and calls this extension a hypothesis requiring validation. That admission is retained; the absence of a justified microscopic closure is not presented as a newly discovered source error.

Conserved island flux \(RB_\perp\), volume filling, and a merger-controlled lifetime are assumptions. Under them, \(\tau_{\rm rec}\propto R^2/B_\perp\) implies \(d\mathcal E/dt\propto-\mathcal E^{5/2}\), hence \(\mathcal E\propto t^{-2/3}\), \(R\propto t^{1/3}\) and \(B_\perp\propto t^{-1/3}\). The corresponding fixed-rate MHD algebra gives the stated \(t^{-1}\) energy law. Critical balance with fixed model coefficients gives \(l\propto R/B_\perp\), hence \(t^{2/3}\). These exponent controls are retained.

The equipartition/advection-time comparison suppresses order-one temperature factors and is supported by equal-temperature runs. It should not be read as a uniform prefactor identity across arbitrarily extreme \(T_i/T_e\). This does not change the time exponents at a fixed temperature ratio.

Several tempting criticisms are excluded. Finite-FLR density advection is not exactly zero, but its cancellation is explicitly used as a subion approximation, and the source distinguishes its empirical near-transition agreement from a large-separation derivation. Isothermal \(g_e=0\) is explicitly acknowledged not to solve the full kinetic equation in a turbulent/reconnecting state; the source tests its approximation with a nonisothermal comparison. Hyperdiffusion, finite scale separation and the beta ordering are disclosed. Normalized structure-function prefactors and a global multiplicative normalization of the local-field direction cancel from the normalized diagnostics and are not an independent material finding here.

## Reproducibility and evidence boundary

verify_equation_consistency.py is an original standard-library program that imports no other verifier or source implementation. It checks three linear-symbol cases, eight exact periodic energy witnesses, the Gaussian/Hermite projection, dimensional vectors, and eight positive rate/ERMHD parameter sets. It evolves no plasma and contains no source numerical data. The generated equation-consistency-checks.json binds its bytes and source identities.

Printed main inconsistencies are verified in v2 and selected AM pages. Supplementary findings are verified only in the supplied v2 supplement and its page pixels. The subscription VOR and any final journal supplement remain outside this review's verified identity scope. No original simulations, experimental claims, hidden implementation or numerical reconnection/decay result is rejected.

## Bounded publication judgment

A short technical consistency comment on these named editions is supportable. Its contribution would be reproducibility: the displayed main system cannot reduce to its stated Appendix system, and the supplied kinetic hierarchy and purported invariant fail direct projections or local conservation tests. The most substantive organization is three related clusters: main-system dimensional/sign consistency; the collisionless Hermite projection; and the density-energy coefficient. The subsidiary beta definition and parallel-term coefficient can be documented without presenting each as an independent new physical result.

The strongest counterargument is that these are recognizable display defects in an otherwise standard model: Appendix A already carries the consistent core coefficients/signs, and an expert implementation may use the correct established equations. The source's cited KREHM literature, especially Zocco and Schekochihin (2011), owns the underlying model and invariant, not the proposed comment. That original paper was not independently reread in this particular derivation assignment; the proofs above follow directly from the inspected source expressions, and a separate primary-reference check should bind the historical comparison before publication. The Gaussian and conservation identities are standard mathematics, not novel plasma theory.

Accordingly, a title, abstract and conclusions should identify arXiv:2407.06020v2, the inspected publisher accepted manuscript, and the v2 supplement precisely. A claim about errors remaining in the uninspected subscription VOR or final journal supplement is unwarranted. No manuscript, submission, DOI deposit or publication action was performed in this review.
