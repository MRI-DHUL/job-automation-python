import streamlit as st
import pandas as pd

def render_export(jobs):

    st.subheader("Export Results")

    df = pd.DataFrame(jobs)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download CSV",
        csv,
        "jobs.csv",
        "text/csv"
    )

    json_data = df.to_json(orient="records")

    st.download_button(
        "Download JSON",
        json_data,
        "jobs.json",
        "application/json"
    )