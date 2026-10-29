# Reproduction

Run from any working directory; the program locates this package from its own path. It reads no source PDF, external dataset, network service or other verifier. Do not use Python `-O`: assertions enforce exact identities, and optimized execution is explicitly rejected.

All exact equation checks use Python's standard library and rational `Fraction` arithmetic:

```powershell
python reproduction/run_audit.py --no-plots
```

To regenerate the same checks and both PNG figures, install the plotting requirements and run:

```powershell
python -m pip install -r requirements.txt
python reproduction/run_audit.py
```

The producer overwrites its own five JSON/CSV outputs under `data/` and, without `--no-plots`, its two figures. Numerical fractions are serialized as exact strings. The JSON embeds the producer's SHA-256. It includes recorded source identities with an explicit recorded-not-rehashed declaration; it does not pretend to revalidate absent source PDFs. No timestamps or interpreter-specific metadata enter those five deterministic numerical outputs.

The original producer was run with CPython 3.12.14, NumPy 2.3.5 and Matplotlib 3.11.2 for figures. An independent standard-library execution with CPython 3.13.7 checks that its five numerical files are byte-identical. Actual run evidence is recorded separately in `data/runtime-environments.json`. This is a two-runtime verification, not a claim that a combined SciPy environment was tested. SciPy is not required by the producer.

Independent copied verifiers, if present under `audit/`, have their own documented entry points, original hashes and execution receipts. They are not imported by the producer. Read their provenance before rerunning; they may write their own adjacent results. Their source identities remain recorded provenance rather than a fresh download assertion.

The package is computational preparation only. It provides no original GX inputs, output fields or raw diagnostic arrays. It does not reproduce a published plasma simulation or verify the subscription journal VOR.
