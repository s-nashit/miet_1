import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

st.title('My App')
df = pd.read_csv('placement.csv')
df.drop('College_ID', axis='columns', inplace=True)
df['Internship_Experience']=df['Internship_Experience'].apply(lambda x: 1 if x == 'Yes' else 0)
df['Placement'] = df['Placement'].apply(lambda x: 1 if x == 'Yes' else 0)
x = df.drop('Placement', axis='columns')
y = df['Placement']
model = LogisticRegression()
model.fit(x,y)

iq = st.number_input('Enter IQ')
prev = st.number_input('Previous GPA')
cgpa = st.number_input('Enter CGPA')
acad = st.number_input('Enter Performance')
inter = st.number_input('Enter Internship')
eca = st.number_input('ECA')
cs = st.number_input('Comm')
projects = st.number_input('No of projects')

