import os

import httpx
import streamlit as st
from bokeh.models.widgets import Div


APP_URL = os.environ["APP_URL"]
STRAVA_CLIENT_ID = os.environ["STRAVA_CLIENT_ID"]
STRAVA_CLIENT_SECRET = os.environ["STRAVA_CLIENT_SECRET"]
STRAVA_AUTHORIZATION_URL = "https://www.strava.com/oauth/authorize"


def authorization_url():
    request = httpx.Request(
        method="GET",
        url=STRAVA_AUTHORIZATION_URL,
        params={
            "client_id": STRAVA_CLIENT_ID,
            "redirect_uri": APP_URL,
            "response_type": "code",
            "approval_prompt": "auto",
            "scope": "activity:read_all"
        }
    )

    return request.url


def login_header(header=None):
    strava_authorization_url = authorization_url()

    if header is None:
        base = st
    else:
        _, _, _, button = header
        base = button

    if base.button("Login with Strava"):
        js = f"window.location.href = '{strava_authorization_url}'"
        html = f"<img src onerror=\"{js}\">"
        div = Div(text=html)
        st.bokeh_chart(div)


def logout_header(header=None):
    if header is None:
        base = st
    else:
        _, _, _, button = header
        base = button

    if base.button("Logout of Strava"):
        js = f"window.location.href = '{APP_URL}'"
        html = f"<img src onerror=\"{js}\">"
        div = Div(text=html)
        st.bokeh_chart(div)


def authenticate(header=None):
    query_params = st.experimental_get_query_params()
    authorization_code = query_params.get("code", [None])[0]

    if authorization_code is None:
        login_header(header=header)
        st.stop()
    else:
        logout_header(header=header)
        response = httpx.post(
            url="https://www.strava.com/oauth/token",
            json={
                "client_id": STRAVA_CLIENT_ID,
                "client_secret": STRAVA_CLIENT_SECRET,
                "code": authorization_code,
                "grant_type": "authorization_code",
            }
        )
        response.raise_for_status()

        return response.json()

def header():
    col1, col2, col3 = st.beta_columns(3)
    with col3:
        strava_button = st.empty()

    return col1, col2, col3, strava_button
