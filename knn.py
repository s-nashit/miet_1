import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder

st.title('My KNN Model')
df = pd.read_csv('employee.csv')
df.dropna(inplace =True)
le = LabelEncoder()
df['Department'] = le.fit_transform(df['Department'])
df.drop('EmployeeID', axis='columns', inplace = True)
x = df.drop('Stays (1=Yes, 0=No)', axis='columns')
y = df['Stays (1=Yes, 0=No)']
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()
model.fit(x,y)

age = st.number_input('Enter age')
salary = st.number_input('Enter Salary')
exp = st.number_input('Enter years')
dept = st.number_input('Enter Dept: (0-HR; 1-IT; 2-Sales)')

pred = model.predict([[age, salary, exp, dept]])

if st.button('Analyse'):
    if pred == 1:
        st.success('You are doing good')
    else:
        st.info('Chances of layoff')