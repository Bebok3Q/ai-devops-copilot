import spacy
from sentence_transformers import SentenceTransformer, util

# Load NLP models
nlp = spacy.load("en_core_web_sm")
model = SentenceTransformer('all-MiniLM-L6-v2')

# Simulated error → fix pairs
known_errors = {
    "ModuleNotFoundError": "Check if the module is installed and listed in requirements.txt.",
    "Out of memory": "Increase memory limit in CI pipeline or optimize the process.",
    "Timeout": "Consider increasing the timeout limit in CI settings.",
    "Permission denied": "Check file or directory permissions.",
    "ImportError": "Ensure the module is correctly imported and exists."
}

# Precompute embeddings
known_error_texts = list(known_errors.keys())
known_embeddings = model.encode(known_error_texts)

def analyze_log(log_text: str):
    doc = nlp(log_text)
    error_lines = [sent.text for sent in doc.sents if "error" in sent.text.lower() or "exception" in sent.text.lower()]
    is_anomalous = bool(error_lines)  # Log uznawany za anomalny, jeśli zawiera linie z błędami

    main_error = error_lines[0] if error_lines else "No clear error message detected."
    likely_cause = None
    suggested_fix = None

    if error_lines:
        # Find the most similar known error only if error lines are detected
        error_embedding = model.encode([main_error])
        similarity_scores = util.cos_sim(error_embedding, known_embeddings)[0]
        best_match_index = similarity_scores.argmax().item()
        likely_cause = known_error_texts[best_match_index]
        suggested_fix = known_errors[likely_cause]

    return {
        "error_message": main_error,
        "likely_cause": likely_cause,
        "suggested_fix": suggested_fix,
        "is_anomalous": is_anomalous
    }