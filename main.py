import streamlit as st

import strava


st.set_page_config(
    page_title="Streamlit-Strava",
    page_icon=":chart_with_upwards_trend:",
)

st.image("https://analytics.gssns.io/pixel.png")

st.markdown(
    """
    # Streamlit-Strava
    """
)

strava_auth = strava.authenticate()

st.write("You are logged in")
st.write(strava_auth)
