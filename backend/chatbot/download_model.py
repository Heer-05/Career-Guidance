"""
download_model.py
-----------------
Downloads the DistilBERT intent classifier model from Google Drive.
Run this once on Render during the build step.
"""

import os
from pathlib import Path

MODEL_DIR = Path(__file__).parent / "intent_classifier"
MODEL_FILE = MODEL_DIR / "model.safetensors"
FILE_ID = "1XbvQtB0m87EMlQ3AWO3QP3Z-88yPtdkT"  # paste your file ID here

def download_model():
    if MODEL_FILE.exists():
        print("Model already exists, skipping download.")
        return
    try:
        import gdown
    except ImportError:
        # torch/transformers are not installed on the free-tier deploy, so the
        # chatbot uses its keyword fallback and the model would never be loaded
        print("gdown not installed, skipping model download (chatbot uses keyword fallback).")
        return
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    print("Downloading DistilBERT model from Google Drive...")
    url = f"https://drive.google.com/uc?id={FILE_ID}"
    gdown.download(url, str(MODEL_FILE), quiet=False)
    print("Model downloaded successfully.")

if __name__ == "__main__":
    download_model()