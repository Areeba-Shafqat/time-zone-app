# import required libraries
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# list of availabe time zones
time_zones=[
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney"
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

# create app title
st.title("Time Zone App")

# create a multi-select dropdown for choosing time zones
selected_timezone = st.multiselect("Select Timezones",time_zones,default=["UTC","Asia/Karachi"])
 
# display current time for selected time zones
st.subheader("Selected Timezones")
for tz in selected_timezone:
    # get and format current time for each selected timezone with AM/PM
    current_time=datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    # display timezone and its current time
    st.write(f"**{tz}**: {current_time}")
    
# create section for time conversion
st.subheader("Convert Time Between Timezones")
# create time input field with current time as default
current_time=st.time_input("Current Time",value=datetime.now().time())
# dropdown to select source timezone
from_tz = st.selectbox("From Timezone",time_zones,index=0)
# dropdown to select target timezone
to_tz= st.selectbox("To Timezone",time_zones,index=1)

# create convert buton and handle conversion
if st.button("Convert Time"):
    # combine today's date with input time and source timezone
    dt= datetime.combine(datetime.today(),current_time,tzinfo=ZoneInfo(from_tz))
    # convert time to target timezone and format it with AM/PM
    converted_time= dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    # display the converted time with success message
    st.success(f"Converted Time in {to_tz}: {converted_time}")
                                   