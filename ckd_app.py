import streamlit as st
import pandas as pd
import joblib  # or use pickle, depending on your model file

# Load your model (update filename as needed)
model = joblib.load('your_model_filename.pkl')  # Change to your actual model filename

st.title("CKD Patient Identification")
st.write("Upload a CSV file with patient data to predict CKD.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Preview of uploaded data:")
    st.dataframe(data.head())

    if st.button('Predict CKD'):
        predictions = model.predict(data)
        data['CKD_Prediction'] = predictions
        st.write("Prediction Results:")
        st.dataframe(data)
        csv = data.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Results as CSV",
            data=csv,
            file_name="ckd_predictions.csv",
            mime="text/csv",
        )
