'''
author         : Rupesh Garsondiya 
github       : @Rupeshgarsondiya
Organization : L.J University
'''





import pandas as pd
import streamlit as st
import numpy as np
from features.build_features import  *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score



class Model_Train:
    def __init__(self) -> None:
        pass

    '''load_data()  fuction use for to get the clean data or feature transformed data '''
    def load_data(self):
        pass
   

    def train_model(self):
        st.markdown(
            """
            <style>
            body {
                background-color: lightblue;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        fe = FeatureEngineering()
        x_train,x_test,y_train,y_test,pipeline = fe.get_clean_data()
       
        
        # Define the options for the dropdown menu
        options = ['Logistic Regreesion', 'Random Forest Classifier', 'Decision Tree', 'SVM','KNeighborsClassifier']
        # Create the dropdown menu
        with st.container():
         st.markdown('<div class="dropdown-left">', unsafe_allow_html=True)
         selected_option = st.sidebar.selectbox('Select Algoritham :', options)
         st.markdown('</div>', unsafe_allow_html=True)

        S_algo  = object
        if selected_option== 'Logistic Regreesion':
            S_algo = LogisticRegression()
            S_algo.fit(x_train,y_train)
            ypred = S_algo.predict(x_test)
        elif selected_option=='Random Forest Classifier':
            S_algo = RandomForestClassifier(n_estimators=200,n_jobs=-1,verbose=True,max_depth=2)
            S_algo.fit(x_train,y_train)
            ypred1 = S_algo.predict(x_test)
        elif selected_option=='Decision Tree':
            S_algo = DecisionTreeClassifier(max_depth=4,max_leaf_nodes=5,min_samples_split=50)
            S_algo.fit(x_train,y_train)
            ypred2 = S_algo.predict(x_test)
        elif selected_option =='SVM':
            S_algo = SVC()
            S_algo.fit(x_train,y_train)
            ypred3 = S_algo.predict(x_test)
        elif selected_option=='KNeighborsClassifier':
            S_algo = KNeighborsClassifier()
            S_algo.fit(x_train,y_train)
            ypred4  = S_algo.predict(x_test)           
        else:
            pass

        return S_algo,pipeline
