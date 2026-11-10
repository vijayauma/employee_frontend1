import streamlit as st
import requests

st.title("Student Management System")

st.subheader("Add Student Details")

name = st.text_input("Enter Student Name")
age = st.number_input("Enter Age", min_value=1, max_value=100)
course = st.text_input("Enter Course")

if st.button("Add Student"):

    if name and course:

        response = requests.post(
            "http://127.0.0.1:8000/add_student",
            params={
                "name": name,
                "age": age,
                "course": course
            }
        )

        if response.status_code == 200:
            st.success("Student added successfully!")

    else:
        st.warning("Please enter all details")


st.subheader("View All Students")

if st.button("Show Students"):

    response = requests.get(
        "http://127.0.0.1:8000/students"
    )

    if response.status_code == 200:

        data = response.json()

        st.table(data)