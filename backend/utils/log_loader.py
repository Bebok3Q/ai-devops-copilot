def load_log_file(filename: str) -> str:
    with open(f"logs/sample_logs/{filename}", "r") as f:
        return f.read()
