import gdown
import os

def download_model():
    model_path = "spit-detection.pt"
    if not os.path.exists(model_path):
        url = "https://drive.google.com/uc?id=1J7efo5zx1MB22DW8K6rGq9MSYVPJn4qj"
        gdown.download(url, model_path, quiet=False)
