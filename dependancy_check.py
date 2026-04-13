import importlib
import shutil

print("🔍 Checking Dependencies...\n")

required_packages = [
    ("torch", "PyTorch"),
    ("torch.nn", "Torch NN"),
    ("torch.nn.functional", "Torch Functional"),
    ("torch.optim", "Torch Optimizer"),
    ("numpy", "NumPy"),
    ("matplotlib.pyplot", "Matplotlib"),
    ("tqdm", "tqdm progress bar"),
    ("torch.utils.data", "Torch Data Utilities")
]

missing = []

for module_name, display_name in required_packages:
    try:
        importlib.import_module(module_name)
        print(f"✅ {display_name} is installed")
    except ImportError:
        print(f"❌ {display_name} is MISSING")
        missing.append(display_name)

# Check unzip availability
print("\n📦 Checking 'unzip' availability...")

if shutil.which("unzip") is not None:
    print("✅ unzip is available")
else:
    print("❌ unzip is NOT available")

# Final summary
print("\n==============================")

if len(missing) == 0:
    print("🎉 All Python dependencies are installed!")
else:
    print("⚠️ Missing packages:")
    for pkg in missing:
        print(f" - {pkg}")

print("==============================")