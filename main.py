import base64

import altair as alt
import streamlit as st

import strava
from pandas.api.types import is_numeric_dtype


st.set_page_config(
    page_title="Streamlit Activity Viewer for Strava",
    page_icon=":circus_tent:",
)

st.image("https://analytics.gssns.io/pixel.png")

strava_header = strava.header()

st.markdown(
    """
    # :circus_tent: Streamlit Activity Viewer for Strava
    """
)

strava_auth = strava.authenticate(header=strava_header, stop_if_unauthenticated=False)

if strava_auth is None:
    st.markdown("Click the \"Connect with Strava\" button to login and get started.")
    st.stop()


activity = strava.select_strava_activity(strava_auth)
data = strava.download_activity(activity, strava_auth)


csv = data.to_csv()
csv_as_base64 = base64.b64encode(csv.encode()).decode()
st.markdown(
    (
        f"<a "
        f"href=\"data:application/octet-stream;base64,{csv_as_base64}\" "
        f"download=\"{activity['id']}.csv\" "
        f"style=\"color:{strava.STRAVA_ORANGE};\""
        f">Download activity as csv file</a>"
    ),
    unsafe_allow_html=True
)


columns = []
for column in data.columns:
    if is_numeric_dtype(data[column]):
        columns.append(column)

selected_columns = st.multiselect(
    label="Select columns to plot",
    options=columns
)

data["index"] = data.index

if selected_columns:
    for column in selected_columns:
        altair_chart = alt.Chart(data).mark_line(color=strava.STRAVA_ORANGE).encode(
            x="index:T",
            y=f"{column}:Q",
        )
        st.altair_chart(altair_chart, use_container_width=True)
