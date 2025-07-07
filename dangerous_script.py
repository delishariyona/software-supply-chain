# 🚨  dangerous_script.py
"""
Intentionally vulnerable code for ML‑risk testing.
DO NOT EXECUTE IN PRODUCTION.
"""

import os
import subprocess
import json

# Hard‑coded credential (looks like AWS key pattern)
SECRET_KEY = "AKIAZXCV1234567890AB"

def nuke_system():
    # Dangerous: deletes everything
    os.system("rm -rf /")  # 🚩

def backdoor(cmd):
    # Dangerous: shell=True with attacker input
    return subprocess.check_output(cmd, shell=True)  # 🚩

def unsafe_eval(user_json: str):
    """
    Takes untrusted JSON, extracts the 'code' field,
    and evals it – classic Remote‑Code‑Execution (RCE) sink.
    """
    data = json.loads(user_json)
    return eval(data["code"])  # 🚩

if __name__ == "__main__":
    print("Backdoor result:", backdoor("echo PWNED"))
    # Build a JSON string safely for the demo
    payload = json.dumps({"code": "__import__('os').getcwd()"})
    print("Eval result:", unsafe_eval(payload))
