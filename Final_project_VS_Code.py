# -*- coding: utf-8 -*-
"""
Created on TUESDAY July 24 22:55:26 2024

@author: RICHIE
"""

import numpy as np
import pickle
import streamlit as st


# #loading the saved model
loaded_model = pickle.load(open("Nigerian_Car_Prices_dataset.zip", "rb"))


def performance_prediction(input_data):

    input_data = (3, 0, 24, 2008, 2, 5750, 2, 9, 2, 6, 201)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array so the model will understand I am making prediction for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    return(f"{prediction} is the price of the Used car") 

def main():

    # giving the app a title
    st.title("Nigeria car price performance Web App")

    # getting the input data from user

    FUEL_TYPE = st.text_input("The Type of fuel PETROL") 
    GEAR_TYPE = st.text_input("Automatic or Manuel")
    MAKE = st.text_input("Make of the car")
    YEAR_OF_MANUFACTURE = st.text_input("the year the car was manufacture")
    CONDITION = st.text_input("Nigeria or Foreign Used")
    ENGINE_SIZE = st.text_input("Size of the Engine")
    BOUGHT_CONDITION = st.text_input("Registered or Imported")
    CAR = st.text_input("Car Name")
    DRIVETRAIN = st.text_input("the different type of Wheel")
    NUMBER_OF_CYLINDER = st.text_input("The number of the car cylinder")
    HORSE_POWER = st.text_input("Horse power number")
    
    # code for Prediction
    performance = ""

    # creating a button for prediction

    if st.button("PRICE RESULT"):
        performance = performance_prediction(
            [FUEL_TYPE, GEAR_TYPE, MAKE, YEAR_OF_MANUFACTURE, CONDITION, ENGINE_SIZE, BOUGHT_CONDITION, CAR, DRIVETRAIN, NUMBER_OF_CYLINDER, HORSE_POWER]) 
        st.success(performance)


if __name__ == "__main__":
    main()

    
    