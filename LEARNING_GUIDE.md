# JourneyMark — learning guide

## What it does

Compare marketing attribution assumptions. The intended user is growth analysts. Browser controls → validated Flask API → project analysis/workflow → results and export.

## Run and demonstrate

Follow the README installation block, then: Compare all four models, shorten the lookback, and inspect the unattributed share. Confirm allocated credits equal conversion count and revenue totals remain unchanged.

## Important files

- `app.py` — local HTTP interface and request/error handling.
- `core.py` — project-specific logic.
- `tests/` — regression and correctness checks.
- `reports/` — recorded outputs and verification evidence.

## Three engineering decisions

1. Allocate each conversion using a documented lookback boundary and exclude touches before a prior conversion.
2. Preserve unattributed conversions rather than dropping their revenue.
3. Compare first, last, linear and time-decay models while testing conservation of credit and revenue.

## Five interview questions

1. **What problem does this project solve, and what is its unit of work?** Explain compare marketing attribution assumptions, identify growth analysts as the audience, and trace one concrete example through the files above. Use the demonstration output rather than hypothetical impact.
2. **Why did you choose the first design decision?** Allocate each conversion using a documented lookback boundary and exclude touches before a prior conversion. Show the corresponding implementation and a test that would fail if that property were removed.
3. **How do you protect correctness when inputs or execution change?** Preserve unattributed conversions rather than dropping their revenue. Explain the relevant invalid-input or edge-case test and distinguish a checked property from an untested assumption.
4. **How do you make results inspectable and reproducible?** Compare first, last, linear and time-decay models while testing conservation of credit and revenue. Point to actual outputs and recorded commands. Explain why a successful example is weaker evidence than a tested boundary or independently reconciled total.
5. **What would you improve before real deployment or real-data use?** Synthetic paths and spend. Attribution is descriptive allocation, not incrementality or causal ROI. No identity stitching, view-through impressions, cross-device behavior or consent workflow. Choose one limitation, describe the missing evidence, and propose a measurable acceptance check rather than promising production readiness.

## Independent exercise

Add a position-based model and reuse the conservation tests.

Write down the expected behavior before editing. Add a meaningful regression check, run the existing suite, and describe what changed in your own words.

## Contribution and resume guidance

The implementation was developed with substantial AI assistance under Abhijith Viswanathan's direction. The verified contribution is the working artifact and the learning work actually completed, not invented employment or adoption.

Suggested factual bullet after personally validating the demo:

- Implemented and validated compare marketing attribution assumptions using pandas · Flask, with first/last/linear/time-decay models and documented correctness checks and limitations.

Use [VERIFICATION.md](VERIFICATION.md) to add only measured numbers. Do not claim production traffic, users, savings, upstream acceptance or cloud deployment without corresponding evidence.
