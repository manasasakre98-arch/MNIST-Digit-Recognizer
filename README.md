# 🔢 MNIST Digit Recognizer

### A CNN-powered handwritten digit recognition web app

![Python](https://img.shields.io/badge/Python-3.x-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange)
![Keras](https://img.shields.io/badge/Keras-Model-red)
![Streamlit](https://img.shields.io/badge/Streamlit-App-ff4b4b)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 📖 Overview

**MNIST Digit Recognizer** is a hands-on deep learning project built to understand and compare the performance of an **Artificial Neural Network (ANN)** and a **Convolutional Neural Network (CNN)** on the classic MNIST handwritten digit dataset.

The project began as a learning experiment: first training an ANN, then a CNN, and comparing their results. The trained CNN model was then integrated into an interactive **Streamlit** web application, allowing users to draw digits by hand and get real-time predictions.

---

## 🎨 Demo / Application Capabilities

The application lets you:

- Draw a digit (0–9) on an interactive canvas
- Get an instant prediction from the trained CNN
- View the model's confidence score
- See the full probability distribution across all 10 digit classes
- Preview the processed 28×28 image used for prediction


---

## ✨ Features

- 🖌️ Interactive 280×280 drawing canvas
- 🔢 Supports digits 0–9
- ⚫ Converts drawing to grayscale
- 📐 Resizes image from 280×280 → 28×28
- 🔧 Normalizes pixel values (0–255 → 0–1)
- 🧩 Reshapes image to CNN input shape `(1, 28, 28, 1)`
- ⚡ Real-time digit prediction
- 📊 Prediction confidence score
- 📈 Probability distribution for all 10 classes
- 🖼️ Processed 28×28 image preview

---

## 🧠 Model Architecture
Input: 28 × 28 × 1
↓
Conv2D (32 filters, 3×3, ReLU)
↓
Output: 26 × 26 × 32
↓
MaxPooling2D (2×2)
↓
Output: 13 × 13 × 32
↓
Flatten
↓
5408 features
↓
Dense (64 neurons, ReLU)
↓
Dense (10 neurons, Softmax)
↓
Predicted Digit


### 📋 Layer Details

| Layer | Type | Parameters | Output Shape |
|-------|------|------------|---------------|
| Input | — | — | 28 × 28 × 1 |
| Conv2D | Convolution | 32 filters, 3×3 kernel, ReLU | 26 × 26 × 32 |
| MaxPooling2D | Pooling | 2×2 pool size | 13 × 13 × 32 |
| Flatten | Flatten | — | 5408 |
| Dense | Fully Connected | 64 neurons, ReLU | 64 |
| Dense (Output) | Fully Connected | 10 neurons, Softmax | 10 |

---

## 📊 Model Performance

| Model | Accuracy |
|-------|----------|
| ANN | 94.72% |
| **CNN** | **97.99%** |

*Evaluated on the 10,000-image MNIST held-out test set.*

### Additional Analysis Performed
- Training/validation accuracy analysis
- Training/validation loss analysis
- Confusion matrix
- Misclassified digit analysis
- CNN convolution feature-map visualization

---

## ⚙️ How It Works

1. Loads the saved CNN model from `mnist_cnn.keras`
2. Provides a Streamlit drawing canvas
3. Receives the user's handwritten digit
4. Converts the image to grayscale
5. Resizes it to 28×28
6. Normalizes the pixel values
7. Reshapes it to `(1, 28, 28, 1)`
8. Passes it through the CNN
9. Uses NumPy `argmax` to determine the predicted digit
10. Displays the prediction and confidence
11. Displays probabilities for all 10 classes

---

## 🛠️ Technologies Used

| Category | Tools |
|----------|-------|
| Language | Python |
| Deep Learning | TensorFlow, Keras |
| Web App | Streamlit |
| Data Processing | NumPy, Pillow |
| Evaluation | Scikit-learn, Matplotlib |

---

## 📁 Project Structure
MNIST-Digit-Recognizer/
│
├── app.py
├── mnist_cnn.keras
├── requirements.txt
└── README.md


---

## 💻 Installation

1. Clone the repository:
```bash
   git clone <your-repository-url>
   cd MNIST-Digit-Recognizer
```

2. Create and activate a virtual environment *(optional but recommended)*:
```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
   pip install -r requirements.txt
```

### 📦 Requirements
streamlit
tensorflow
streamlit-drawable-canvas
numpy
pillow


---

## ▶️ Running the Application

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal (typically `http://localhost:8501`) in your browser.

---

## 🧪 Experiments

- Compared ANN vs. CNN performance on the same dataset
- Analyzed training and validation accuracy/loss curves
- Generated a confusion matrix to identify commonly confused digits
- Reviewed misclassified digit samples to understand model weaknesses
- Visualized CNN convolution feature maps to interpret what the model learns at each layer

---

## 🎓 Learning Outcomes

Through this project, I gained practical understanding of:

- MNIST dataset handling
- Image preprocessing techniques
- Pixel normalization
- One-hot encoding
- Artificial Neural Networks (ANN)
- Convolutional Neural Networks (CNN)
- Convolution filters and feature maps
- Max pooling
- Flattening
- ReLU and Softmax activation functions
- Categorical cross-entropy loss
- SGD / gradient descent optimization
- Model evaluation techniques
- Confusion matrix interpretation
- Model saving and loading
- Integrating a trained Deep Learning model into a Streamlit application

---

## 🚀 Future Improvements

- Better handwriting preprocessing
- Digit centering and scaling
- Improved UI/UX
- Webcam-based digit recognition
- Online deployment
- Experimenting with deeper CNN architectures

---
## 🚀 Live Demo

👉 [Try the MNIST Digit Recognizer](https://mnist-digit-recognizer-09.streamlit.app/)

Draw a handwritten digit and see the CNN predict it in real time!

## 👤 Author

**Manasa**
Computer Science Engineering Student

---

⭐ *If you found this project helpful, consider giving it a star!*
