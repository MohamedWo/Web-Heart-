
# # python -m streamlit run 'Predict_HeartDisease.py'

import pickle
import streamlit as st
import pandas as pd
import pickle

with open("Car_Predict.sav", "rb") as f:
    data = pickle.load(f)

data = pickle.load(open(r'C:\Users\jddkd\OneDrive\Desktop\Project_AI\Diabetes_prediction.sav', 'rb'))

st.title('Diabetes Prediction Web App')
st.info('Easy Application For Predicting Diabetes Disease')

st.sidebar.header('Feature selecting')

Pregnancies = st.text_input('Pregnancies', '')
Glucose = st.text_input('Glucose', '')
BloodPressure = st.text_input('BloodPressure', '')
SkinThickness = st.text_input('SkinThickness', '')
BMI = st.text_input('BMI', '')
DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction', '')
Age = st.text_input('Age', '')

# تحويل المدخلات إلى القيم الصحيحة
def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return None  # إذا كانت القيمة غير قابلة للتحويل، نعيد None

# تحويل المدخلات إلى أرقام
Pregnancies = convert_to_float(Pregnancies)
Glucose = convert_to_float(Glucose)
BloodPressure = convert_to_float(BloodPressure)
SkinThickness = convert_to_float(SkinThickness)
BMI = convert_to_float(BMI)
DiabetesPedigreeFunction = convert_to_float(DiabetesPedigreeFunction)
Age = convert_to_float(Age)

# إنشاء DataFrame للمدخلات
df = pd.DataFrame({
    'Pregnancies': [Pregnancies],
    'Glucose': [Glucose],
    'BloodPressure': [BloodPressure],
    'SkinThickness': [SkinThickness],
    'BMI': [BMI],
    'DiabetesPedigreeFunction': [DiabetesPedigreeFunction],
    'Age': [Age]
}, index=[0])

# التحقق من أن جميع المدخلات صالحة
if df.isnull().values.any():
    st.sidebar.error('Please fill all the fields with valid numbers!')
else:
    # زر تأكيد
    Conf = st.sidebar.button('Confirm')

    if Conf:
        # التنبؤ باستخدام النموذج
        result = data.predict(df)
        if result == 0:
            st.sidebar.write('The Patient is Clear')
            st.sidebar.image('https://astrologer.swayamvaralaya.com/wp-content/uploads/2012/08/health1.jpg', width=150)
        else:
            st.sidebar.write('The Patient Has Disease')
            st.sidebar.image('https://brghealth.com/brg/wp-content/uploads/2020/01/diabetes.png', width=150)

