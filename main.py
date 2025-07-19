import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('placement.csv')
df.drop('College_ID', axis='columns', inplace=True)
df['Internship_Experience']=df['Internship_Experience'].apply(lambda x: 1 if x == 'Yes' else 0)
df['Placement'] = df['Placement'].apply(lambda x: 1 if x == 'Yes' else 0)

x= df.drop('Placement', axis='columns')
y=df['Placement']

model = LogisticRegression()
model.fit(x,y)
st.title('My Logistic Regression')

# IQ	Prev_Sem_Result	CGPA	Academic_Performance	Internship_Experience	Extra_Curricular_Score	Communication_Skills	Projects_Completed

iq = st.number_input('Enter Your IQ')
prev = st.number_input('Enter previous grade')
cgpa = st.number_input('Enter CGPA')
perf = st.number_input('Enter Performance')
intern = st.number_input('Enter no of internships')
eca = st.number_input('Enter ECA Score')
cs = st.number_input('Enter Communication Score')
proj = st.number_input('Enter the number of projects')

pred = model.predict([[iq, prev, cgpa, perf, intern, eca, cs, proj]])

if st.button('Analyse'):
    if pred == 1:
        st.success('Placement done')
    else:
        st.warning('Not placed')
