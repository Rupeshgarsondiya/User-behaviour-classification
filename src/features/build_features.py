'''
Author       : Rupesh Garsondiya
github       : @Rupeshgarsondiya
Organization : L.J university

'''

# Feature  Engineering

# import library

import pandas as pd
import numpy as np
import streamlit as st
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline,make_pipeline
from  sklearn.compose import  ColumnTransformer


'''create class FeatureEngineering is  created to perform feature engineering on the dataset'''
class  FeatureEngineering:

    def __init__(self): # define  constructor
        pass

    def cleandata(self):
        data  = pd.read_csv('/home/rupeshgarsondiya/workstation/lab/Project-1/Data/user_behavior_dataset.csv') # load Dataset
       
        data.drop('User ID',axis=1,inplace=True)  # Drop user id column it not required

        '''Rename column name'''
        data.rename(columns={'Device Model':'P_Model','Operating System':'OS','App Usage Time (min/day)':'App_Time(hours/day)',
                   'Screen On Time (hours/day)':'(hours/Screen_timeday)','Battery Drain (mAh/day)':'Battery_Drain(mAh/day)',
                   'Number of Apps Installed':'Installed_app','Data Usage (MB/day)':'Data_Usage(GB/day)'},inplace=True)
        
        # App time convert minit into the hours 
        data['App_Time(hours/day)']=data['App_Time(hours/day)']/60

        # convert data use MB into GB
        data['Data_Usage(GB/day)']=data['Data_Usage(GB/day)']/1024

        return data
    
    def get_clean_data(self):
        df  =  FeatureEngineering().cleandata()
        print(df.head())

        X = df.drop('User Behavior Class', axis=1)
        y = df['User Behavior Class']

        x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
        
        categorical_col = ['P_Model','OS','Gender']
        categorical_transform = OneHotEncoder()

        numerical_col = ['Battery_Drain(mAh/day)']
        numerical_transform = StandardScaler()

        # use to column transformer to perform onehotencoing and  standard scaling
        preprocessor = ColumnTransformer(
        transformers=[
        
        ('cat', categorical_transform, categorical_col)
         ],remainder='passthrough')
        
        # create sklearn pipeline
        pipeline = Pipeline(steps=[('preprocessor', preprocessor)])
        pipeline.fit(x_train)
        pipeline.fit(x_test)
        x_train_t = pipeline.transform(x_train)
        x_test_t = pipeline.transform(x_test)
        

        return x_train_t,x_test_t,y_train,y_test,pipeline 
    



