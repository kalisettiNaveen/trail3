import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import numpy as np


st.title("Diabetic Retinopathy Detection")


st.sidebar.title("Navigation")
option = st.sidebar.radio("Select an option", ["Home", "Upload Image", "Analytics", "About"])


if option == "Home":
    st.write("### Welcome to the Diabetic Retinopathy Detection")
    st.write("This dashboard helps in detecting diabetic retinopathy using AI-based image analysis.")
    st.image("/Users/kumarimahithakalisetti/Downloads/images.jpeg", caption="Example of Diabetic Retinopathy")
elif option == "Upload Image":
    st.write("### Upload Retinal Image for Analysis")
    uploaded_file = st.file_uploader("Choose a retinal image", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Retinal Image", use_column_width=True)
        st.write("Processing Image...")
        prediction = np.random.choice(["No DR", "Mild DR", "Moderate DR", "Severe DR", "Proliferative DR"], p=[0.5, 0.2, 0.15, 0.1, 0.05])
        st.write(f"### Diagnosis Result: {prediction}")
        
        if prediction != "No DR":
            st.warning("Consult a healthcare professional for further evaluation.")

elif option == "Analytics":
    st.write("### Diabetic Retinopathy Analytics")
    
    data = {
        "Condition": ["No DR", "Mild DR", "Moderate DR", "Severe DR", "Proliferative DR"],
        "Patients": [500, 150, 120, 80, 50]
    }
    df = pd.DataFrame(data)
    
    fig, ax = plt.subplots()
    sns.barplot(x="Condition", y="Patients", data=df, ax=ax, palette="coolwarm")
    ax.set_ylabel("Number of Patients")
    ax.set_title("Distribution of Diabetic Retinopathy Cases")
    st.pyplot(fig)
elif option == "About":
    st.write("### About This Dashboard")
    st.write("This dashboard is developed to assist in detecting diabetic retinopathy using AI-based image processing techniques.")
    st.write("**Developed by:** Your Name")
    st.write("**Contact:** your.email@example.com")