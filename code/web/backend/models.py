"""Allowlisted model configurations shared by saved and live assessments."""

LLAMA = "llama3.1:8b"
QWEN = "Qwen3.6-35B-A3B-MLX-8bit"
MODELS = {
    LLAMA: {"id": LLAMA, "label": "Llama 3.1 8B", "provider": "Local Ollama", "suffix": ""},
    QWEN: {"id": QWEN, "label": "Qwen3.6 35B", "provider": "University KISTE", "suffix": "_" + QWEN},
}


def model_config(model=LLAMA):
    if model not in MODELS:
        raise ValueError("Unknown assessment model.")
    return MODELS[model]


def result_filename(stem, model=LLAMA):
    return stem + model_config(model)["suffix"] + ".csv"
