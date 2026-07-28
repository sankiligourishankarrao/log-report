# log-report
Fix broken Terminal-Bench 2 (Harbor) log-report task
Repairs all authoring defects so the task is reproducible and graded honestly:
- task.toml: artifacts is now a top-level array pointing at the real output (/app/report.json)
- Dockerfile: pin approved base image by @sha256 digest; remove leaked solution_hint.py
- verifier: assert real outcome values (not just file existence); write reward to /logs/verifier/reward.txt + ctrf.json
- instruction.md: unambiguous prompt with absolute paths, named output, numbered criteria, and enforced timeout line

Verified with Harbor 0.18.0: oracle reward 1, nop reward 0, wrong solution reward 0, clean agent image.
