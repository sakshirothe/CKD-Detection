import streamlit as st
import pandas as pd
import joblib

# Load your trained model
MODEL_FILENAME = "ckd_model.pkl"  # update to your actual filename
model = joblib.load(MODEL_FILENAME)

st.title("CKD Patient Identification")
st.write("Upload a CSV file with patient data to predict CKD.")

# Example required columns
required_columns = ["age", "bp", "albumin", "sugar", "hemoglobin"]

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    try:
        data = pd.read_csv(uploaded_file)

        # Check required columns
        missing_cols = [col for col in required_columns if col not in data.columns]
        if missing_cols:
            st.error(f"Missing required columns: {', '.join(missing_cols)}")
        else:
            st.write("Preview of uploaded data:")
            st.dataframe(data.head())

            if st.button("Predict CKD"):
                predictions = model.predict(data[required_columns])
                data["CKD_Prediction"] = predictions
                st.success("Prediction complete!")
                st.dataframe(data)

                # Allow download of results
                csv = data.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="Download Results as CSV",
                    data=csv,
                    file_name="ckd_predictions.csv",
                    mime="text/csv",
                )

    except Exception as e:
        st.error(f"Error reading file: {e}")
