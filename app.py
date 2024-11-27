import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('modelprediksidiabetes.pkl')

# Title and description
st.title("🩺 Prediksi diabetes")
st.markdown("""
### Website Prediksi Diabetes
Aplikasi ini menggunakan model Machine Learning (**Random Forest**) untuk memprediksi apakah seseorang berisiko terkena diabetes atau tidak. 
Masukkan data pada form di bawah ini, lalu klik tombol **Predict** untuk melihat hasilnya.
""")

# Create a form for user input
with st.form("prediction_form"):
    st.header("📝 Masukkan Data Pasien")

    # Input fields in columns
    col1, col2 = st.columns(2)

    with col1:
        Pregnancies = st.text_input("Jumlah Kehamilan (Pregnancies):", value="-")
        Glucose = st.text_input("Kadar Glukosa (Glucose):", value="-")
        BloodPressure = st.text_input("Tekanan Darah (BloodPressure):", value="-")
        SkinThickness = st.text_input("Ketebalan Kulit (SkinThickness):", value="-")

    with col2:
        Insulin = st.text_input("Kadar Insulin (Insulin):", value="-")
        BMI = st.text_input("BMI:", value="-")
        DiabetesPedigreeFunction = st.text_input("Fungsi Silsilah Diabetes:", value="-")
        Age = st.text_input("Usia (Age):", value="-")

    # Submit button
    submit = st.form_submit_button("Predict")

# Prediction logic
if submit:
    try:
        # Check if any input is still "-"
        inputs = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        if "-" in inputs or "" in inputs:
            st.warning("⚠️ Harap isi semua data dengan benar sebelum melanjutkan!")
        else:
            # Convert inputs to float
            input_data = pd.DataFrame({
                'Pregnancies': [float(Pregnancies.replace(",", "."))],
                'Glucose': [float(Glucose.replace(",", "."))],
                'BloodPressure': [float(BloodPressure.replace(",", "."))],
                'SkinThickness': [float(SkinThickness.replace(",", "."))],
                'Insulin': [float(Insulin.replace(",", "."))],
                'BMI': [float(BMI.replace(",", "."))],
                'DiabetesPedigreeFunction': [float(DiabetesPedigreeFunction.replace(",", "."))],
                'Age': [float(Age.replace(",", "."))]
            })

            # Make prediction
            prediction = model.predict(input_data)

            # Display result with style
            st.subheader("🔍 Hasil Prediksi")
            if prediction[0] == 1:
                st.error("❌ Pasien berisiko terkena diabetes.")
            else:
                st.success("✅ Pasien tidak berisiko terkena diabetes.")

    except ValueError:
        st.error("⚠️ Harap masukkan nilai numerik yang valid (gunakan titik/koma untuk desimal).")

# Footer
st.markdown("""
---
💡 **Catatan**: Model prediksi ini tidak menggantikan diagnosis medis profesional. 
Silakan konsultasikan hasil ini dengan dokter untuk kepastian lebih lanjut.
""")
