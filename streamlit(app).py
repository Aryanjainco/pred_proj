import streamlit as st 
import time as t 

st.title("Welcome to health prediction app")
st.write("Fill necessary details")

st.text_input("Enter your email address")

st.radio("Pick your gender",["Male","Female"])

st.slider("Enter ur age",0,100)

st.multiselect("Choose the Disease",["Diabetes","Breast cancer"])


st.file_uploader("Upload your adhaar card")

st.checkbox('Save details')

st.button("Sign up")

st.select_slider("Rating for the app",["Really Good","Almost accurate","Need improvement","Really bad"])

st.text_area("Any suggestions for improvement")

with st.spinner("Submitting"):
    t.sleep(2)

st.balloons()

st.sidebar.title("Already have an account?")
st.sidebar.text_input("Email address")
st.sidebar.text_input("Password")
st.sidebar.button("LOGIN")