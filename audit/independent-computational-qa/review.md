# Independent computational review

The frozen producer and output tables pass an independent, read-only standard-library check. The reviewer read the complete producer, computational methods, reproduction instructions and README, and visually inspected both final PNG figures. No producer or other verifier is imported or executed by the new output checker. This is a separate check of a finite synthetic family, not a source simulation or a claim about the uninspected VOR.

## Separate calculation

For the reported family A=a cos(mx)+b cos(ny), N=h sin(mx) sin(ny), the reviewer derives the exchange I=habmn(m²−n²)/4 directly from trigonometric averages. The original-mode coefficients of the flux derivative are

    Fdot_x = −κ b h m n [Te+Ti+Ti d² n²]/2,
    Fdot_y =  κ a h m n [Te+Ti+Ti d² m²]/2.

Dividing by 1+d²m² and 1+d²n² gives the vector-potential derivatives entering the magnetic and electron-inertia energy derivatives. This calculation does not use Fourier convolution. The six-mode inertial-advection squared norm is independently 3(κ Ti d²)²(C²+D²)/16, with C=ahm³n and D=bhmn³. It confirms all 60 rows, including 36 nonzero-exchange states and 24 zero controls. The root state gives Udot=21/20, Kedot=39/20, Kidot=Yhalf_dot=−3/2, consistent total zero, and doubled-density total −3/2. All inertia terms retained by the producer are included. The de²=0 cases are mathematical limiting controls.

Twenty-four real-phase linear symbols reproduce the opposite signs of the two time-evolution eigenvalue squares after restoring the dimensional pressure coefficient. Finite Γ0 belongs to these linear-symbol controls; the nonlinear energy family uses the strict-subion closure. The audit does not call that nonlinear family a finite-FLR simulation.

For Gaussian/Hermite controls, the independent checker constructs Hm from its explicit factorial sum rather than the producer's recurrence. Exact Gaussian factorial moments reproduce all 81 orthogonality pairs, nine drive projections and six neighboring-streaming magnitudes/signs. Collisions remain identically zero. Eight rate/ERMHD parameter sets and two conditional decay regimes also agree. Every row and field of all four CSV tables agrees with the JSON. The 24 historical source/review records retain their manifest hashes.

## Normalization and scope

The energy controls use an energy-normalized potential varphi=e phi_physical. Thus varphi=−Ti N, κ=c/(e B0), G=1/(4π), and α=e de²/(c me B0) satisfy Gκ=n0α. The rational tests set the corresponding dimensionless e=1 and G=1. If varphi is instead read as the dimensional electric potential, its advective coefficient is c/B0; those two notations must not be mixed. The current code is mathematically consistent; making the energy-normalized potential explicit in the explanatory methods is a documentation clarification.

Both figures are legible, have unclipped axes/legends, and distinguish synthetic controls from source runs. The wave panel is a prescribed analytical cos/cosh illustration, not a nonlinear stability calculation. The Hermite panel is a collisionless identity illustration, not a heating calculation.

The accepted manuscript remains distinct from the subscription VOR. Supplemental findings remain limited to arXiv v2. Appendix A and the established KREHM/ERMHD literature already supply the consistent conventions; the source's supported rates, conditional exponents and explicit model qualifications are retained. No numerical curves, actual GX implementation or final journal supplement are invalidated by this verification.

No scientific or code blocker was found. The numerical output hashes, figure hashes, independent program and final documentation bytes are bound in the accompanying machine-readable receipts.
