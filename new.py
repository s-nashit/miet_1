import streamlit as st
import pickle

with open('knn.pkl', 'rb') as f:
    model = pickle.load(f)

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