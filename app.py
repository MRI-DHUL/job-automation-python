import streamlit as st
from services.job_service import search_jobs
from ui.sidebar import render_sidebar
from ui.results import render_results
from ui.exporter import render_export

st.set_page_config(page_title="AI Job Finder", layout="wide")

st.title("Job Automation Tool")

filters, search_clicked = render_sidebar()

if search_clicked:

    with st.spinner("Fetching jobs..."):

        jobs = search_jobs(filters)

        st.session_state["jobs"] = jobs


if "jobs" in st.session_state:

    jobs = st.session_state["jobs"]

    render_results(jobs)
    render_export(jobs)