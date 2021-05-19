import os

import streamlit as st


STRAVA_CLIENT_ID = os.environ["STRAVA_CLIENT_ID"]
STRAVA_CLIENT_SECRET = os.environ["STRAVA_CLIENT_SECRET"]


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
