@@ -0,0 +1,16 @@
#!/bin/bash

# pytest is baked into the environment image (environment/Dockerfile).
mkdir -p /logs/verifier

pytest /tests/test_outputs.py -rA --ctrf /logs/verifier/ctrf.json
rc=$?

if [ "$rc" -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

# Always exit 0 — pass/fail lives in reward.txt.
exit 0
