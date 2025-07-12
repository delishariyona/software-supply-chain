# utils/ml_engine.py

def analyze_commit(diff_text, filenames):
    # Simulated ML result logic
    if "eval" in diff_text or "exec" in diff_text:
        severity = "High"
        confidence = 0.95
    elif "import os" in diff_text:
        severity = "Medium"
        confidence = 0.7
    else:
        severity = "Low"
        confidence = 0.3

    return {
        "severity": severity,
        "confidence": round(confidence, 2),
        "ml_score": int(confidence * 100),
        "features_used": ["CodeBERT (simulated)"]
    }
