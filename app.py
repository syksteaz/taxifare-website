import datetime
import streamlit as st
import requests  
import pandas as pd

st.title("🚕 Taxi ride pricer 🚕")
st.subheader("Predict how much you will pay for a ride in NYC🗽")

#ask for date and time
# d = st.date_input("When do you want to ride", datetime.date(2019, 7, 6))
d = st.date_input("Day of ride", datetime.date(2024, 5, 31))
# t = st.time_input('Set an alarm for', datetime.time(8, 45))
t = st.time_input('Time of ride?')
pickup_datetime = f"{d} {t}"

#Pikcup & dropoff longitude and latitude ? 
# http://localhost:8000/predict?pickup_datetime=2014-07-06+19:18:00&pickup_longitude=-73.950655&pickup_latitude=40.783282&dropoff_longitude=-73.984365&dropoff_latitude=40.769802&passenger_count=2
pickup_longitude = st.number_input("Pickup longitude?", key="pickup_longitude", value=73.950655, placeholder=73.950655, format='%.6f')
pickup_latitude = st.number_input("Pickup longitude?", key="pickup_latitude", value=40.783282, placeholder=40.783282)


dropoff_longitude = st.number_input("Drop-off longitude?", key="dropoff_longitude", value=73.984365, placeholder=73.984365)
dropoff_latitude = st.number_input("Drop-off longitude?", key="dropoff_latitude", value=40.769802, placeholder=40.769802)

#What's the passenger count? 
passenger_count = st.selectbox(
    "How many riders will be in da car?",
    (1, 2, 3, 4, 5, 6))



## Once we have these, let's call our API in order to retrieve a prediction
url = 'https://taxifare.lewagon.ai/predict?'
#2. Let's build a dictionary containing the parameters for our API...
params = {
    "pickup_datetime":pickup_datetime,
    "pickup_longitude":pickup_longitude,
    "pickup_latitude":pickup_latitude,
    "dropoff_longitude":dropoff_longitude,
    "dropoff_latitude":dropoff_latitude, 
    "passenger_count":passenger_count
}

#3. Let's call our API using the `requests` package...

st.button(label='Get ride price',key="fare")

if st.session_state.get("fare"):
    r = requests.get(url, params=params)
    st.info(round(r.json()['fare'],2))
## here we need a button to send the data


#4. Let's retrieve the prediction from the **JSON** returned by the API...


## Finally, we can display the prediction to the user