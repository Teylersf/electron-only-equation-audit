# Bounded primary-theory verification for source 10

## Sources and actual reading scope

**KREHM primary:** A. Zocco and A. A. Schekochihin, *Reduced fluid-kinetic equations for low-frequency dynamics, magnetic reconnection, and electron heating in low-beta plasmas*, Physics of Plasmas **18**,102309 (2011), DOI [10.1063/1.3628639](https://doi.org/10.1063/1.3628639). The UKAEA-hosted [published PDF](https://scientific-publications.ukaea.uk/wp-content/uploads/Published/POPVOL18p102309.pdf) was retrieved normally, HTTP200,675,100bytes, SHA-256`6ca81472979b0506571dd22f435cd5a7c5f1a802b4d62b35a91717e801735735`. It has an added publisher cover and24 article pages. I read the relevant ordering, electron-moment/closure, kinetic, energy and Hermite material: SectionsII.B,III.A–E,IV.A–C andV.A–C. These are principally PDFpp5–13, printed102309-4 through102309-12, with limited nearby context. I do **not** claim to have read all later tearing appendices or the whole paper. Its official [arXiv record1104.4622](https://arxiv.org/abs/1104.4622) identifies v2 as matching the published version; that version's compressed single-file TeX was also retrieved for source-form verification.

**ERMHD primary:** A. A. Schekochihin et al., *Astrophysical gyrokinetics: kinetic and fluid turbulent cascades in magnetized weakly collisional plasmas*, Astrophysical Journal Supplement Series **182**,310 (2009), DOI [10.1088/0067-0049/182/1/310](https://doi.org/10.1088/0067-0049/182/1/310). The [official arXiv record0704.0044](https://arxiv.org/abs/0704.0044) says v4 was replaced to match the published version. Its arXiv PDF is1,903,708bytes,SHA-256`47419fbdeea137d73844c47557239f73753410cbf6f5e4b47d66bfb463ef1569`,67pages. I read the relevant convention/parameter passages and Sections7.1–7.8: principally pp8,11,21 and30–34. Its exact v4 TeX archive was retrieved as well. This is a bounded section read, **not** a claim to have read all67pages, nor an independent byte-identity check against a publisher VOR PDF.

Target scope is the inspected arXiv2407.06020v2, its embedded supplement, and the authentic CHORUS accepted manuscript. The target's subscription VOR and final journal supplement remain unavailable. The third-party source PDFs/TeX are reading evidence, not newly authored or relicensed material.

## Convention matching comes before signs

Set `q=delta n_e/n_0e`, `theta=delta T_parallel,e/T_0e`, `A=A_parallel=A_z`, and `u=(e/(c*m_e))*d_e^2*Delta_perp A`, where `e` is the positive elementary charge. Both KREHM and the target define

\[
\{f,g\}=\partial_xf\partial_yg-\partial_yf\partial_xg,\quad
D_t=\partial_t+\frac{c}{B_0}\{\varphi,\cdot\},\quad
\mathcal D_\parallel=\partial_z-\frac1{B_0}\{A,\cdot\}.
\]

In KREHM these are Eqs(5),(31),(32), with magnetic perturbation `delta B_perp=-z_hat cross grad_perp A`. The target's printed parallel derivative is the same, and it supplies the same electron-flow/Ampere relation. KREHM Eqs(37),(38) give `j_parallel=-c*Delta_perp A/(4*pi)=-e*n_0e*u` after neglecting parallel ion flow. Thus a silent `A -> -A` or bracket reversal is **not** an explanation unless the magnetic field, parallel derivative and Ampere/velocity relation are all transformed consistently.

For the AGK paper the flux function has the opposite sign: Eq(135),p21 gives `Phi=c*varphi/B_0` and `Psi=-A/sqrt(4*pi*m_i*n_0i)`. Its derivative `partial_z+{Psi,.}/v_A`, Eq(20),p8, therefore becomes exactly the minus-A-bracket derivative above. Comparing its plus-Psi bracket directly to the target without this conversion would manufacture a sign error.

## 1. Continuity: the density form has a minus

KREHM Eq(39), printed102309-6/PDF7, is

\[
D_tq+\mathcal D_\parallel u_{\parallel i}
=-\mathcal D_\parallel\left(\frac{e d_e^2}{c m_e}\Delta_\perp A\right).
\]

Its Eq(58) sets the parallel ion flow to zero at the retained order. This is also directly electron number conservation `D_tq=-D_parallel u` with the stated electron velocity. The target's mainEq(1) and supplementEq(7) print the opposite sign in that density form. In contrast, its AppendixA Eq(A1) has a **positive**2D A-bracket, which is consistent with the corrected minus-parallel-derivative equation because in2D `D_parallel=-{A,.}/B_0`.

A particularly important counterargument is KREHM's summaryEq(62), printed102309-8/PDF9: it does have a **positive**parallel derivative on its RHS. However, its LHS evolves the polarization variable `P*varphi=-(delta n/n)`, using quasineutralityEq(56). Replacing that polarization variable by density without its minus is not an equivalent copying ofEq(62). Both primary equations are mutually consistent; the dependent variable matters.

This supports a correction to the **printed density equation under the displayed conventions**. It does not establish which sign GX actually evolved, and is not proof of a false numerical result.

## 2. The dimensional pressure term carries c*T_0e/e

KREHM Eq(40), printed102309-6/PDF7, has the positive pressure contribution

\[
D_t(A-d_e^2\Delta_\perp A)
=-c\partial_z\varphi
+\frac{cT_{0e}}e\mathcal D_\parallel(q+\theta)
+\hbox{collisional/ion-flow terms}.
\]

Its summaryEq(63) says the same after substituting its negative polarization-density relation. The target's mainEq(2) and supplementEq(8) omit `c*T_0e/e`; targetA2 restores it in its2D rewrite. Dimensional quantities and the same variable definitions cannot obey both printed versions as written.

**Counterargument:** a normalization could make this coefficient numerically one. Such a model must declare the potential/vector-potential/time units and apply the conversion consistently. The target retains physical `c,e,T,m` factors in neighboring definitions and inA2 and introduces dimensionless simulation units later. An unspecified coefficient-one convention cannot reconcile its dimensional formulas without additional information. The defensible finding is a dimensional/presentation inconsistency, not a claim that normalized source code must be wrong.

## 3. Density free energy: Y has a half

KREHM Eq(68), printed102309-9/PDF10, defines the quadratic kinetic free energy with `T*delta f^2/(2F_0)`. Inserting its distribution decompositionEq(69) yields Eq(70), and Eqs(71),(72),(76) preserve the same weights:

\[
Y=\int\frac{d^3r}{V}\frac{n_{0e}T_{0e}}2q^2.
\]

The target supplementEq(12), p8/combinedPDF17, prints `n_0e*T_0e*q^2` without the half while retaining the usual weights of `U,K_i,K_e` and writing their simple sum as the conservedW. This is not a harmless **overall**rescaling of the invariant.

There is an independent internal normalization control. In the sub-ion limit for singly charged ions, quasineutrality gives `q=-e*varphi/T_0i`. Then

\[
K_i=\int\frac{d^3r}{V}\frac{n_{0e}e^2\varphi^2}{2T_{0i}},\qquad
Y_{\rm standard}=\frac{T_{0e}}{T_{0i}}K_i.
\]

At equal temperatures the primary normalization gives `K_i=Y`; the target's printedY instead gives `Y_printed=2K_i`. The target's following Section5 argument invokes `K_i approximately Y`, consistent with the primary normalization. **Counterargument:** one may define a diagnostic namedY to be twice the standard value, but then it must enterW with weight1/2 or the remaining definitions must change. RenamingY alone cannot make the printed unweighted sum the standard invariant. No claim is made that Figure8's actual arrays used the erroneous printed coefficient; a display-only omission remains possible, and order-of-magnitude equipartition/scaling is not refuted by this factor alone.

## 4. Collisionless Hermite signs are fixed by the given expansion

KREHM Eq(64), printed102309-8/PDF9, and Eq(42),PDF7, give

\[
D_tg+v_\parallel\mathcal D_\parallel(g-\theta F_0)
=C[g]+(1-2x^2)F_0\mathcal D_\parallel u,
\qquad x=v_\parallel/v_{\rm the}.
\]

Its Hermite conventions are Eqs(86)–(90), printed102309-11/PDF12: physicists' `H_m(x)`, coefficients of `H_m/sqrt(2^m m!)`, and `theta=sqrt(2)*g_2`. The resultingEq(93),printed102309-12/PDF13, is

\[
D_tg_m+v_{\rm the}\mathcal D_\parallel
\left(\sqrt{\frac{m+1}{2}}g_{m+1}+\sqrt{\frac m2}g_{m-1}
-\delta_{m1}g_2\right)
=-\sqrt2\,\delta_{m2}\mathcal D_\parallel u+C_m.
\]

The forcing sign can be checked without relying on transcription: `H_2=4x^2-2`, so `(1-2x^2)=-H_2/2` has normalized Hermite coefficient `-sqrt(2)`. Equivalently Gaussian moments `<x^2>=1/2`, `<x^4>=3/4` give `<H_2*(1-2x^2)>/sqrt(8)=-sqrt(2)`. The temperature moment is therefore

\[
D_t\theta+\sqrt3\,v_{\rm the}\mathcal D_\parallel g_3
=-2\mathcal D_\parallel u
\]

in the collisionless case, matching primaryEq(94).

Target supplementEq(11),combinedPDF15, puts **positive**streaming and **positive**`sqrt(2)`forcing on the RHS. Its own kineticEq(9), when specialized to2D, has the primary LHS streaming sign and the primary source. Moving streaming to the RHS thus gives a minus, not the printed plus. The discrepancy remains with collisions set to zero and is independent of a convention for the sign of a damping operator namedC.

**Counterarguments:** rephasing odd Hermite coefficients or reversing the velocity coordinate can reverse a streaming matrix representation, but does not turn the even`m=2`source positive while retaining the given expansion, temperature moment and physical velocity. More generally, the phase transformation needed to reverse both the matrix and forcing would make `g_2=-theta/sqrt(2)`, contrary to those definitions. A global coordinate reversal must transform the derivative and velocity together. These are not available silent repairs of the displayed equations. Conversely, reversing the streaming matrix alone is not proof of an instability or failed Landau damping; no such claim is made.

The omitted explicit`partial_z`streaming in targetEq(9) is not promoted here as a separate error: its non-isothermal experiment is expressly2D, where that derivative vanishes. Likewise, the notation `-C[g_m]` alone is not promoted as a collision-sign error without an explicit definition of that transformed operator. No actual numerical Hermite implementation is recovered.

## 5. ERMHD beta and the proposed finite-beta rate

AGK Eq(42),p11, unambiguously defines

\[
\beta_i=\frac{v_{\rm thi}^2}{v_A^2}
=\frac{8\pi n_{0i}T_{0i}}{B_0^2},
\quad v_{\rm thi}^2=2T_{0i}/m_i,
\quad \beta_e=(Z/\tau)\beta_i.
\]

The target supplement p3/combinedPDF12 instead prints `4*pi*n_0i*m_i/B_z^2`, which is `1/v_A^2` in these dimensional conventions. A thermal-speed-squared factor is needed to obtain the dimensionless beta. Using a thermal speed without the square-root2 convention can move a factor2, but cannot supply a missing dimension. An explicitly declared unit choice `v_thi=1` could explain the numerical shorthand; no such definition is given in this physical-form ERMHD passage. Treat this as a displayed parameter-definition problem, not a demonstrated error in an assigned numerical beta.

There is a substantive **positive**control: with standard beta and the conversion `Phi=c*varphi/B_0`, `Psi=-A/sqrt(4*pi*m_i*n_0i)`, AGK Eqs(221),(222),(226),(227),pp30–31, reduce in2D to the target supplement's two ERMHD equations. In particular its **positive2Dbracket**in the density equation is correct. The apparent opposite sign in the AGK Psi notation disappears after the minus relation betweenPsi andA is applied.

AGK Eq(230),p31, gives the KAW coefficient proportional to

\[
\rho_i\sqrt{\frac{1+Z/\tau}{2+\beta_i(1+Z/\tau)}}.
\]

Since `rho_i=sqrt(beta_i)*d_i`, this has exactly the beta dependence of the target's proposed rate multiplied byR:

\[
\mathcal R_{\rm proposed}\sim
\sqrt{\frac{\beta_i(1+Z/\tau)}{2+\beta_i(1+Z/\tau)}}\frac{d_i}{R}.
\]

ForZ=1 its low-beta limit is `rho_i/R*sqrt((1+1/tau)/2)`, identical to mainEq(4), `sqrt(1+tau)*rho_s/R`. This is an algebraic consistency control, **not**a derivation of a reconnecting solution from flux-frozen ERMHD.

AGK Sections7.6–7.7,pp33–34, explicitly delimit the electron-scale expansion, neglected damping and flux freezing; electron inertia, electron FLR or resistivity must ultimately break flux. The target supplement itself clearly acknowledges this obstruction, presents its rate as a hypothesis, and asks for further numerical validation. Its two-point comparison with an assumed half-box island size is limited support, not a universal validated high-beta law. It would be inaccurate to allege that the target silently overlooked the need for flux breaking, or that this primary comparison disproves its rate hypothesis.

## Overall bounded conclusion

The target-cited GX framework has independently verified primary identification: N. R. Mandell et al., *GX: a GPU-native gyrokinetic turbulence code for tokamak and stellarator design*, arXiv2209.06731 (v1 dated14September2022; current v5 dated29April2024), subsequently JPP **90**(4),905900402 (2024), DOI [10.1017/S0022377824000631](https://doi.org/10.1017/S0022377824000631), published online23September2024. Its official abstract identifies GPU-native nonlinear gyrokinetics and a phase-space pseudospectral Laguerre–Hermite method. The publisher's first footnote identifies the source repository as [bitbucket.org/gyrokinetics/gx](https://bitbucket.org/gyrokinetics/gx), with documentation at [gx.readthedocs.io](https://gx.readthedocs.io/en/latest/). This is a bounded metadata/abstract/citation check, not a full GX paper or code audit. No current branch, commit, input file or standard benchmark is identified as the target's actual run version. The absence of target run inputs must not be described as absence of an identified or public solver framework.

The primary references substantiate the continuity minus, dimensional Ohm coefficient, half-weighted density energy and collisionless Hermite signs under the target's explicitly matching conventions. They also provide positive ERMHD structure and low-beta-limit checks. These are discrepancies in the **inspected printed preprint/accepted-manuscript/supplement definitions**. They do not establish what GX executed, whether final VOR typesetting repaired them, or that any plotted curve or central inverse-transfer result is false. No long-paper whole-read, source-author contact, source-code replication, new simulation or publication is claimed.
