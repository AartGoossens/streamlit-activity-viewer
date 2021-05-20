import streamlit as st
import sweat

import strava


st.set_page_config(
    page_title="Streamlit-Strava",
    page_icon=":chart_with_upwards_trend:",
)

st.image("https://analytics.gssns.io/pixel.png")

strava_header = strava.header()

st.markdown(
    """
    # Streamlit-Strava
    """
)

strava_auth = strava.authenticate(header=strava_header)


activity = strava.select_strava_activity(strava_auth)

if activity is None:
    st.stop()

data = sweat.read_strava(activity["id"], strava_auth["access_token"])

columns = []
for column in ["heartrate", "power"]:
    if column in data.columns:
        columns.append(column)

st.line_chart(data[columns])
