# -*- coding: utf-8 -*-
"""
Created on Thur July  17 22:55:26 2024

@author: RICHIE
"""

import numpy as np
import pickle
import streamlit as st


# #loading the saved model
loaded_model = pickle.load(open("Financial_model.sav", "rb"))


def performance_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array so the model will understand I am making prediction for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return("This individual is not eligible to have bank account")
    else:
        return("This individual is eligible to have bank account")


def main():

    # giving the app a title
    st.title("Financial Inclusion in Africa")

    # getting the input data from user

    country = st.text_input("What country are you from? 0 for Kenya/1 for Rwanda/2 for Tanzania/3 for Uganda")
    location_type = st.text_input("What is your locality? 0 for rural/1 for urban")
    cellphone_access = st.text_input("Do you have phone access? 1 for yes/0 for no")
    household_size = st.text_input("What is the size of your house hold?")
    age_of_respondent = st.text_input("What is your age?")
    gender_of_respondent = st.text_input("What is your gender? 1 for male/0 for female")
    relationship_with_head	 = st.text_input("What is your relationship with the head? 0 for Spouse/1 for Head of Household/2 for Other relative/3 for Child/4 for Parent/5 for Other non-relatives")
    marital_status = st.text_input("What is your marital status? 0 for Married/Living together/1 for Widowed/2 for Single/Never Married/3 for Divorced/Seperated/4 Dont know")
    education_level = st.text_input("What level of education do you have? 0 for Secondary education/1 for No formal education/2 for Vocational/Specialised training/3 Primary education/4 for Tertiary education/5 for Other/Dont know/RTA")
    job_type = st.text_input("What type of job do you have? 0 for Self employed/1 for Government Dependent/2 for Formally employed Private/3 for Informally employed/4 for Formally employed Government/5 for Farming and Fishing/6 for Remittance Dependent/7 for Other Income/8 for Dont Know/Refuse to answer/9 No Income")
    
    # Gender_Female = st.text_input("Is learner's gender female ?")
    # Gender_Male = st.text_input("Is learner's gender male")

    # code for Prediction
    performance = ""

    # creating a button for prediction

    if st.button("CHURN RESULT"):
        performance = performance_prediction(
            [country, location_type , cellphone_access, household_size, age_of_respondent, gender_of_respondent, relationship_with_head, marital_status, education_level, job_type ])
        st.success(performance)


if __name__ == "__main__":
    main()
