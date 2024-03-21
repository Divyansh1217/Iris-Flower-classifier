from sklearn.model_selection import train_test_split as tts
from sklearn.neighbors import KNeighborsClassifier as knn
import pandas as pd
import streamlit as st
st.set_page_config(layout='wide')
data=pd.read_csv('C:/Users/divya/Desktop/New folder/Iris/IRIS.csv')
x=data.drop('species',axis=1)
y=data['species']
x_train,x_test,y_train,y_test=tts(x,y,test_size=0.2,random_state=42)
Knn=knn(n_neighbors=1)
Knn.fit(x_train,y_train)
sep_l=st.number_input("Sepal length")
sep_w=st.number_input("Sepal width")
pet_l=st.number_input("Petal length")
pet_w=st.number_input("Petal Width")
import numpy as np
new_a=np.array([[sep_l,sep_w,pet_l,pet_w]])
prediction=Knn.predict(new_a)
st.write(prediction)