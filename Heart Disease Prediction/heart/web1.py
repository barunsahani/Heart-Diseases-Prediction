import os
import pickle 
import streamlit as st    
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="🧑‍⚕️")
heart_model= pickle.load(open(r"C:\Users\Barun\OneDrive\Desktop\Heart Disease Prediction\heart\training_model\heart_model.sav",'rb'))

with st.sidebar:
    selected= option_menu('Prediction of disease outbreak system',
                          ['Heart Prediction'],
                          menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)
    
if selected == 'Heart Prediction':
        st.title('Heart Prediction')

        col1, col2, col3=st.columns(3)

        with col1:
            age=st.text_input('Age')

        with col2:
             sex=st.text_input('Sex')

        with col3:
             cp=st.text_input('Chest Pain Types')

        with col1:
             trestbps=st.text_input('Resting Blood Pressure')

        with col2:
             chol=st.text_input('Serum Cholestoreal in mg/d1')

        with col3:
             fbs=st.text_input('Fasting Blood Sugar')

        with col1:
             restecg=st.text_input('Resting Electtrocardiographpicresults')

        with col2:
             thalach=st.text_input('Maximum Heart Rate Achieved')

        with col3:
             exang=st.text_input('Exercise Induced Angina')

        with col1:
             oldpeak=st.text_input('ST Depression Induced by Exercise Relative to Rest')

        with col2:
             slope=st.text_input('The Slope of the Peak Exercise ST Segment')

        with col3:
             ca=st.text_input('Number of Major Vessels Colored by Flourosopy')

        with col1:
             thal=st.text_input('thal:0=normal;1=fixed defect;2=reversable defect')


        heart_diagnosis=''


        if st.button('Heart Disease Prediction'):

             user_input=[age,sex, cp,trestbps,chol,fbs,restecg,
                         thalach,exang,oldpeak,slope,ca,thal]
             
             user_input=[float(x) for x in user_input]


             heart_prediction=heart_model.predict([user_input]) # type: ignore

             if heart_prediction[0]==1:
                heart_diagnosis='You have Heart Disease'
             else:
                heart_diagnosis='You do not have Heart Disease'

        st.success(heart_diagnosis)        
                
