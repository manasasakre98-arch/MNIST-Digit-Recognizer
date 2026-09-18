import streamlit as st
from tensorflow.keras.models import load_model
from streamlit_drawable_canvas import st_canvas
import matplotlib.pyplot as plt

st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .prediction-box {
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

model = load_model("mnist_cnn.keras")

st.markdown(
    '<div class="main-title">✍️ MNIST Digit Recognizer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Draw a handwritten digit and let the CNN recognize it.</div>',
    unsafe_allow_html=True
)

st.subheader("About the Model")

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("CNN Accuracy", "97.99%")

with col2:
    st.metric("ANN Accuracy", "94.72%")

with col3:
    st.metric("Dataset","MNIST")

with col4:
    st.metric("Classes", "10")

st.subheader("Draw a digit")

st.caption("Use your mouse to draw a single digit from 0 to 9.")

canvas = st_canvas(
    fill_color="black",
    stroke_width=15,
    stroke_color="white",
    background_color="black",
    height=280,
    width=280,
    drawing_mode="freedraw",
    return_image_data=True,
    key="canvas",
)

if canvas.image_data is not None:
    image = canvas.image_data

    # Convert RGBA to grayscale
    gray = image[:, :, 0]

    # Resize to MNIST dimensions
    from PIL import Image
    resized = Image.fromarray(
        gray.astype("uint8")
    ).resize((28, 28))


    # Convert image to NumPy array
    import numpy as np
    image_array = np.array(resized).astype("float32")

    # Normalize pixel values to 0–1
    image_array /= 255.0

    input_image = image_array.reshape(1,28,28,1)

    st.subheader("Processed Image")
    st.image(image_array, width=150)

    prediction = model.predict(input_image, verbose=0)

    predicted_digit = np.argmax(prediction)

    confidence = np.max(prediction)*100

    st.subheader("Prediction")
    st.success(f"Digit: {predicted_digit} | Confidence: {confidence:.2f}%")

    st.subheader("Class Probabilities")

    probabilities = prediction[0] * 100

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.bar(range(10), probabilities)
    ax.set_xticks(range(10))
    ax.set_xlabel("Digit")
    ax.set_ylabel("Probability (%)")
    ax.set_ylim(0, 100)
    ax.set_title("Prediction Probability Distribution")

    st.pyplot(fig)

