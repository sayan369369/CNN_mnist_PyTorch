# CNN on MNIST with PyTorch 🧠

A Convolutional Neural Network (CNN) built from scratch using PyTorch, 
trained to classify handwritten digits from the MNIST dataset.

## 🏗️ Model Architecture

| Layer | Details |
|-------|---------|
| Conv1 | 1→16 channels, 3×3 kernel, ReLU + MaxPool 2×2 |
| Conv2 | 16→32 channels, 3×3 kernel, ReLU + MaxPool 2×2 |
| FC1 | 128 units, ReLU |
| Dropout | Rate: 0.3 |
| FC2 (Output) | 10 classes |

## 📦 Requirements

Run the dependency checker first:
```bash
python dependancy_check.py
```

**Dependencies:** PyTorch, NumPy, Matplotlib, tqdm

## 🚀 How to Run

1. Clone the repo
2. Place `mnist.npz` in the same folder
3. Open `assignment3.ipynb` in Jupyter or VS Code
4. Run all cells

## 📊 Dataset

MNIST — 70,000 grayscale images of handwritten digits (0–9), 28×28 pixels.
