import streamlit as st
import pandas as pd 
import numpy as np
from streamlit_folium import st_folium
from sklearn.experimental import enable_iterative_imputer 
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer,KNNImputer,IterativeImputer
from sklearn.preprocessing import OneHotEncoder,LabelEncoder,OrdinalEncoder
from sklearn.preprocessing import StandardScaler,MinMaxScaler,Normalizer
from sklearn.model_selection import train_test_split
import joblib


model=joblib.load("model2")

title=st.title("hous price predicsion in tehran")

mantage=st.text_input("Enter your mantage in tehran","soleymani")

metrage=st.number_input("Enter your metrage hous")

sal=st.slider(label="select year",min_value=1365, max_value=1406, value=None, step=None, format=None)

otage=st.selectbox(label="Enter the number of rooms",options=[1,2,3,4,5])


tabage=st.slider(label="select the floor",min_value=0,max_value=20)

tehdad_vahed=st.selectbox(label="select the numbrt of vahed",options=[1,2,3,4,5,6,7,8])

col1, col2, col3, col4 = st.columns(4)

with col1:
    vshed_status = st.radio(
        "vahed status",
        ["True", "False"],
        horizontal=False
    )

with col2:
    anbari = st.radio(
        "anbari status",
        ["True", "False"],
        horizontal=False
    )

with col3:
    parking = st.radio(
        "parking status",
        ["True", "False"],
        horizontal=False
    )

with col4:
    asansor = st.radio(
        "asansor status",
        ["True", "False"],
        horizontal=False
    )                                          

lat=st.number_input("Enter your lat of hous")
long=st.number_input("Enter your long of hous")






# itre_ipute=IterativeImputer()
# df=itre_ipute.fit_transform(df)

coloums=["mantage","metrage","sal","otsg","tabage","vshed_status","lat","long","tehdad_vahed","asansor","parking","anbari"]

def predict():


    data = {
        "mantage": [mantage], 
        "metrage": [metrage],
        "sal": [sal],
        "otsg": [otage], 
        "tabage": [tabage],
        "vshed_status": [vshed_status],
        "lat": [lat],
        "long": [long],
        "tehdad_vahed": [tehdad_vahed],
        "asansor": [asansor],
        "parking": [parking],
        "anbari": [anbari]
    }

    X = pd.DataFrame(data)
    le=LabelEncoder()
    X["vshed_status"]=le.fit_transform(X["vshed_status"])
    X["asansor"]=le.fit_transform(X["asansor"])
    X["parking"]=le.fit_transform(X["parking"])
    X["anbari"]=le.fit_transform(X["anbari"])
    X["mantage"]=le.fit_transform(X["mantage"])
    X["tabage"]=le.fit_transform(X["tabage"])
    perd =model.predict(X)

    predictsion =st.write(perd)
but_pred=st.button("predict",on_click=predict)