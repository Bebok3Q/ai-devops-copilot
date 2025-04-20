from typing import Optional

# Simulated knowledge base of fixes
error_fix_db = {
    "ModuleNotFoundError": {
        "patch": "Add 'flask' to requirements.txt",
        "explanation": "The module is not installed. Adding it to requirements will ensure it's installed in CI/CD."
    },
    "Timeout": {
        "patch": "Increase timeout in test runner config (e.g., pytest.ini or CI YAML)",
        "explanation": "Tests might take longer in CI than locally. Increasing timeout can fix it."
    },
    "Permission denied": {
        "patch": "Add chmod +x to shell script or set correct file permissions in CI",
        "explanation": "This error is caused by file permission issues. Ensure executable files have correct access."
    }
}

def suggest_fix(error_text: str) -> Optional[dict]:
    for key in error_fix_db:
        if key.lower() in error_text.lower():
            return {
                "error": key,
                "suggested_patch": error_fix_db[key]["patch"],
                "explanation": error_fix_db[key]["explanation"]
            }
    return None
