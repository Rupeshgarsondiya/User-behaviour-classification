'''
Author       : Rupesh Garsondiya
github       : @Rupeshgarsondiya
Organization : L.J University
'''





import http
import streamlit as st
from PIL import Image
from train import *
from test import *


# Centering the title using HTML and CSS

   
class Main:
    def __init__(self) -> None:
        pass

    def run(self):
        
        # Display the image from a URL
        st.markdown(
            """
            <style>
            .img-rounded {
                border-radius: 15px;
                width: 400px;  /* Adjust the width as needed */
            }
            
            </style>
            <div style="text-align: center;">
            <img src="https://files.oaiusercontent.com/file-j5d0noa13fNCzctwMzacm7k9?se=2024-10-15T17%3A31%3A03Z&sp=r&sv=2024-08-04&sr=b&rscc=max-age%3D604800%2C%20immutable%2C%20private&rscd=attachment%3B%20filename%3D393b3cd9-2488-4f60-a1d7-52fe26428c8f.webp&sig=JSGn0KwxflHJ9MPWGzjpDn%2BzUTJxnMrSN2%2BrrTMhoLg%3D" class="img-rounded",><br>
        
            """,
            unsafe_allow_html=True
        )
        st.write()
        st.write()
        

        t = test()
        t.predict_data()

       
        st.markdown("[GitHub](https://github.com/Rupeshgarsondiya/Project-1) | <a href='https://www.linkedin.com/in/rupesh-garsondiya-919817275/' target='_blank'>Linkedin</a>",unsafe_allow_html=True)
        

        # Add a LinkedIn profile hyperlink using HTML
        st.markdown("", unsafe_allow_html=True)



        
        # Add copyright notice at the bottom
        st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line to separate content
        st.markdown(
            "<b><p style='text-align: center; font-size: 12px;'>&copy; 2024 Rupesh Garsondiya. All Rights Reserved.</p>", 
            unsafe_allow_html=True
        )

        
if  __name__ == "__main__":

    
    
    st.markdown("<h1 style='text-align: center;'><b>User behaviour classification on user Behaviour Dataset</b></h1>", unsafe_allow_html=True)

    st.markdown("<p ><b> - About this project  :</b></p>",unsafe_allow_html=True)
    st.write(' - This project is a simple web application that uses a machine learning model to classify user behavior into different categories.')

    st.write(' - The model is trained on a dataset of user behavior and can be used to  predict the behavior of a new user based on their mobile data.')

    run_obj = Main()
    run_obj.run()

else  : 
    print("This is a Streamlit app. Please run it using `streamlit run app.py `")  # noqa: E501