''''
Author        : Rupesh Garsondiya
github        : @Rupeshgarsondiya
Organization  : L.J University

'''

import time
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing  import StandardScaler
from train import *


class test :
    
    def __init__(self):
        pass
    
    def predict_data(self):
        
        st.sidebar.title("Select Parameter ")
        mt = Model_Train()
        S_algo,Pipeline = mt.train_model()
        df = None
        options = ["Google Pixel 5", "OnePlus 9", "Samsung Galaxy S21", "Xiaomi Mi 11",'iPhone 12']

        selected_option = st.sidebar.selectbox("Select phone model :", options)

        if selected_option in options:
            encoded_model = [1 if  i == selected_option else 0 for i in options]
            df = pd.DataFrame([encoded_model], columns=options)
        


        options1 = ["Android",'IOS']

        
        

        if selected_option =='iPhone 12':
            selected_option1 = st.sidebar.selectbox("Select  OS :", 'IOS')
            encoded_os = [0,1]
        else :
            encoded_os = [1,0]
            selected_option1 = st.sidebar.selectbox("Select  OS :", 'Android')
        df[options1] = encoded_os
        

        options2 = ['Female','Male']
        selected_option2 = st.sidebar.radio("Select Gender :", options2)
        encoded_gender = [1 if  i == selected_option2 else 0 for i in options2]
        df[options2] = encoded_gender


        app_time = st.sidebar.number_input('Enter app time : ',min_value=0.0,max_value=24.0,value=0.0)
        df['App_Time(hours/day)'] = app_time
      

        screen_time = st.sidebar.number_input('Enter your screen  time : ',min_value=0.0,max_value=24.0,value=0.0)
        df['screen_Time(hours/day)'] = screen_time
        

        battary = st.sidebar.number_input('Enter battary drain(mAh) : ',min_value=100.0,max_value=6000.0,value=100.0)
        df['Battery_Drain(mAh)'] = battary
       

        no_app = st.sidebar.number_input('Enter  number of apps installed : ',min_value=5.0,max_value=50.0,value=5.0)
        df['Installed_app'] = no_app


        data_use = st.sidebar.number_input('Enter  data usage (GB) : ',min_value=0.0,max_value=10.0,value=0.0)
        df['Data_Usage(GB)'] = data_use

        
        age = st.sidebar.number_input('Enter your age : ',min_value=15.0,max_value=100.0,value=15.0)
        df['Age'] = age
        
        if st.button("Submit"):
            st.write("Processing...")
            time.sleep(2)
            prediction = S_algo.predict(df)
            if prediction==1:

                st.write('Output :  Occasional Users')
            elif prediction==2:
                 st.write('Output : Casual Users ')
            elif prediction==3:
                st.write('Output : content consumer : ')
            elif prediction==4:
               st.write('Output  :  Social Media Enthusiasts')
            else :
               st.write('Output  : Power Users')
        
        








        




       
      

        
        

        