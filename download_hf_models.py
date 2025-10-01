import os
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM

# --------------------------
# Config
# --------------------------
MODELS = {
    "llama2": "meta-llama/Llama-2-7b-hf",
    "mpt7b": "mosaicml/mpt-7b-instruct",
    "falcon7b": "tiiuae/falcon-7b-instruct"
}

SAVE_DIR = "local_hf_models"
os.makedirs(SAVE_DIR, exist_ok=True)

# --------------------------
# Function to download model
# --------------------------
def download_model(name, repo_id):
    model_path = os.path.join(SAVE_DIR, name)
    if os.path.exists(model_path):
        print(f"✅ Model '{name}' already downloaded at {model_path}")
        return model_path

    print(f"⬇️ Downloading '{name}' from HuggingFace: {repo_id}")
    
    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(repo_id, local_files_only=False)
    # Load model
    if "llama" in name.lower() or "mpt" in name.lower() or "falcon" in name.lower():
        model = AutoModelForCausalLM.from_pretrained(repo_id, device_map="auto", local_files_only=False)
    else:
        model = AutoModelForSeq2SeqLM.from_pretrained(repo_id, device_map="auto", local_files_only=False)

    # Save locally
    tokenizer.save_pretrained(model_path)
    model.save_pretrained(model_path)
    print(f"✅ Model '{name}' saved at {model_path}")
    return model_path

# --------------------------
# Download all models
# --------------------------
if __name__ == "__main__":
    for name, repo in MODELS.items():
        download_model(name, repo)
