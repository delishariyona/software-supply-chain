#!/usr/bin/env python3
"""
run_ml_check.py
-------------------------------------------------
GitHub Action helper that:
1. Computes the diff between BASE_SHA and HEAD_SHA.
2. Passes that diff to utils.ml_engine.analyze_commit().
3. Prints the verdict.
4. Exits with code 1 to fail the check if severity is HIGH. 
"""

import subprocess
import sys
import json
from pathlib import Path

# ---------- 1.  Read commit SHAs from CLI ----------
if len(sys.argv) != 3:
    print("Usage: run_ml_check.py <BASE_SHA> <HEAD_SHA>")
    sys.exit(1)

base_sha = sys.argv[1]
head_sha = sys.argv[2]

# ---------- 2.  Grab diff & filenames ----------
diff = subprocess.check_output(
    ["git", "diff", f"{base_sha}..{head_sha}"], text=True
)
filenames = subprocess.check_output(
    ["git", "diff", "--name-only", f"{base_sha}..{head_sha}"], text=True
).strip().splitlines()

# Guard if diff is empty
if not diff.strip():
    print("⚠️  No diff detected between commits.")
    sys.exit(0)

# ---------- 3.  Run your model ----------
# Assumes utils.ml_engine exists in repo
from utils.ml_engine import analyze_commit   # noqa: E402

result = analyze_commit(diff, filenames)

print("🔍  ML analysis result:")
print(json.dumps(result, indent=2))

# ---------- 4.  Decide pass / fail ----------
if result["severity"].lower() == "high":
    print("❌ High‑risk commit detected – failing status check.")
    sys.exit(1)

print("✅ Commit considered safe enough – passing status check.")
sys.exit(0)
