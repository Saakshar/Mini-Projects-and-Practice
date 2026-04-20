import os
import sys
import traceback

try:
    from groundingdino.util.inference import load_model
except Exception:
    print("ERROR: could not import groundingdino.util.inference")
    traceback.print_exc()
    sys.exit(2)

base_dir = os.path.dirname(__file__)
config_path = os.path.join(base_dir, "groundingdino_config.py")
weights_path = os.path.join(base_dir, "groundingdino_weights.pth")

print(f"Using config: {config_path}")
print(f"Using weights: {weights_path}")

try:
    model = load_model(config_path, weights_path)
    print("Model loaded successfully")
except Exception:
    print("ERROR: failed to load model")
    traceback.print_exc()
    sys.exit(3)
