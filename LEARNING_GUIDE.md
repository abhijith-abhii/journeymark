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

1. **Why compare several attribution models?** First-touch, last-touch, linear and time-decay models encode different assumptions about credit. Differences between them show sensitivity to those assumptions, not which channel caused a purchase.

2. **How are repeated conversions handled?** Eligible touches are bounded by the lookback window and the previous conversion. This prevents an old touch from being reused indiscriminately across repeated purchases.

3. **What happens when no eligible touch exists?** The conversion remains unattributed. Its value is preserved so channel credits plus unattributed value reconcile to the total.

4. **What property do the tests enforce?** Credit conservation across all four models. Allocated value must match eligible conversion value, including the explicit unattributed bucket.

5. **Why is attributed ROAS not causal ROI?** Exposure is not randomly assigned and channel selection is confounded. Attribution assigns credit; estimating incremental return needs an experiment or defensible causal design.

## Independent exercise

Add a position-based model and reuse the conservation tests.

Write down the expected behavior before editing. Add a meaningful regression check, run the existing suite, and describe what changed in your own words.

## Contribution and resume guidance

The implementation was developed with substantial AI assistance under Abhijith Viswanathan's direction. The verified contribution is the working artifact and the learning work actually completed, not invented employment or adoption.

Suggested factual bullet after personally validating the demo:

- Compared four marketing attribution models with lookback and repeat-conversion boundaries; verified credit conservation including unattributed conversion value.

Use [VERIFICATION.md](VERIFICATION.md) to add only measured numbers. Do not claim production traffic, users, savings, upstream acceptance or cloud deployment without corresponding evidence.
