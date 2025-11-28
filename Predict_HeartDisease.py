
# # python -m streamlit run 'Predict_HeartDisease.py'

# import pickle
# import streamlit as st
# import pandas as pd
# import pickle

# with open("Car_Predict.sav", "rb") as f:
#     data = pickle.load(f)



# st.title('Diabetes Prediction Web App')
# st.info('Easy Application For Predicting Diabetes Disease')

# st.sidebar.header('Feature selecting')

# Pregnancies = st.text_input('Pregnancies', '')
# Glucose = st.text_input('Glucose', '')
# BloodPressure = st.text_input('BloodPressure', '')
# SkinThickness = st.text_input('SkinThickness', '')
# BMI = st.text_input('BMI', '')
# DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction', '')
# Age = st.text_input('Age', '')

# # تحويل المدخلات إلى القيم الصحيحة
# def convert_to_float(value):
#     try:
#         return float(value)
#     except ValueError:
#         return None  # إذا كانت القيمة غير قابلة للتحويل، نعيد None

# # تحويل المدخلات إلى أرقام
# Pregnancies = convert_to_float(Pregnancies)
# Glucose = convert_to_float(Glucose)
# BloodPressure = convert_to_float(BloodPressure)
# SkinThickness = convert_to_float(SkinThickness)
# BMI = convert_to_float(BMI)
# DiabetesPedigreeFunction = convert_to_float(DiabetesPedigreeFunction)
# Age = convert_to_float(Age)

# # إنشاء DataFrame للمدخلات
# df = pd.DataFrame({
#     'Pregnancies': [Pregnancies],
#     'Glucose': [Glucose],
#     'BloodPressure': [BloodPressure],
#     'SkinThickness': [SkinThickness],
#     'BMI': [BMI],
#     'DiabetesPedigreeFunction': [DiabetesPedigreeFunction],
#     'Age': [Age]
# }, index=[0])

# # التحقق من أن جميع المدخلات صالحة
# if df.isnull().values.any():
#     st.sidebar.error('Please fill all the fields with valid numbers!')
# else:
#     # زر تأكيد
#     Conf = st.sidebar.button('Confirm')

#     if Conf:
#         # التنبؤ باستخدام النموذج
#         result = data.predict(df)
#         if result == 0:
#             st.sidebar.write('The Patient is Clear')
#             st.sidebar.image('https://astrologer.swayamvaralaya.com/wp-content/uploads/2012/08/health1.jpg', width=150)
#         else:
#             st.sidebar.write('The Patient Has Disease')
#             st.sidebar.image('https://brghealth.com/brg/wp-content/uploads/2020/01/diabetes.png', width=150)

import streamlit as st
import pandas as pd
import pickle
import os

# ====== تحميل النموذج بأمان ======
BASE_DIR = os.path.dirname(__file__)  # مسار الملف الحالي
MODEL_PATH = os.path.join(BASE_DIR, "Car_Predict.sav")

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error(f"Model file not found. Please upload 'Car_Predict.sav' in the app folder.")
    st.stop()  # إيقاف التطبيق إذا الملف مش موجود

# ====== واجهة التطبيق ======
st.title('Diabetes Prediction Web App')
st.info('Easy Application For Predicting Diabetes Disease')

st.sidebar.header('Feature selecting')

# ====== إدخال البيانات ======
Pregnancies = st.sidebar.text_input('Pregnancies', '')
Glucose = st.sidebar.text_input('Glucose', '')
BloodPressure = st.sidebar.text_input('BloodPressure', '')
SkinThickness = st.sidebar.text_input('SkinThickness', '')
BMI = st.sidebar.text_input('BMI', '')
DiabetesPedigreeFunction = st.sidebar.text_input('DiabetesPedigreeFunction', '')
Age = st.sidebar.text_input('Age', '')

# ====== تحويل المدخلات لأرقام ======
def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return None

inputs = {
    'Pregnancies': convert_to_float(Pregnancies),
    'Glucose': convert_to_float(Glucose),
    'BloodPressure': convert_to_float(BloodPressure),
    'SkinThickness': convert_to_float(SkinThickness),
    'BMI': convert_to_float(BMI),
    'DiabetesPedigreeFunction': convert_to_float(DiabetesPedigreeFunction),
    'Age': convert_to_float(Age)
}

# إنشاء DataFrame للمدخلات
df = pd.DataFrame([inputs])

# ====== التحقق من صحة البيانات ======
if df.isnull().values.any():
    st.sidebar.error('Please fill all the fields with valid numbers!')
else:
    if st.sidebar.button('Confirm'):
        # التنبؤ باستخدام النموذج
        result = model.predict(df)[0]  # .predict ترجع قائمة، ناخد أول عنصر

        if result == 0:
            st.success('The Patient is Clear')
            st.image('https://astrologer.swayamvaralaya.com/wp-content/uploads/2012/08/health1.jpg', width=200)
        else:
            st.error('The Patient Has Disease')
            st.image('https://brghealth.com/brg/wp-content/uploads/2020/01/diabetes.png', width=200)


