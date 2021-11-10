# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 03:51:41 2021

@author: ADMIN
"""

import streamlit as st 
import numpy as np 
import pandas as pd 
import plotly.express as px 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.linear_model import LinearRegression,Lasso,Ridge 
from sklearn.model_selection import train_test_split 
st.title('Interest rate subsidy') 
st.text('Check your eligiblity for availing interest rate subsidy') 
df=pd.read_csv('Training Data.csv') 
# The following lines create boxes in which user can enter data required to make prediction
age=st.selectbox ("Age",range(21,80,1)) 
sex = st.radio("Select Gender: ", ('male', 'female')) 
income=st.slider("Income",min_value=0,max_value=10000000,step=50000) 
workex = st.selectbox('Work Experience',range(0,20,1)) 
marital=st.radio('Marital Status',('Yes','No')) 
own=st.selectbox('Ownership status',("not rented/not owned","rented","owned")) 
default = st.radio("Have you ever defaulted in past: ", ('yes', 'no')) 
# user input 
w=0
o=0
a=0
inc=0
d=0
if 0<= workex <=2:
    w = 0 
elif 2<workex<=3:
    w = 1
elif 3<workex<=5:
    w = 2
else:
    w = 3
if own== 'rented':
    o=0
elif own=='not rented/notowned':
    o=1
else:
    o=2
if 0<=income<=100000:
    inc=0
elif 100000<income<=500000:
    inc=1
elif 500000<income<=1000000:
    inc=2
elif 1000000<income<=5000000:
    inc=3
else:
    inc=4
if 21<age<=30:
    a=1
elif 30<age<=50:
    a=2
else:
    a=0
if default=='yes':
    d=-6
else:
    d=0
user_input = w+inc+a+o+d
st.text('Your score is: '+str(user_input)+' out of 11')
if st.button("Predict"):
    if user_input > 8:
        st.text('You are eligible for loans at subsidized interest rates')
    elif 6<=user_input<=8:
        st.text('You are eligible for loans at normal interest rates')    
    else:
        st.text('You are eligible for loans at high interest rates')
    
