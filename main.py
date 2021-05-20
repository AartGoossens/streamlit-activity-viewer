import streamlit as st

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

st.write("You are logged in")
st.write(strava_auth)
