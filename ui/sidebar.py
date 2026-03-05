import streamlit as st


def render_sidebar():

    st.sidebar.header("Job Filters")

    provider = st.sidebar.selectbox(
        "Provider",
        ["all", "remoteok", "remotive", "arbeitnow"]
    )

    keywords = st.sidebar.text_input(
        "Keywords (comma separated)",
        placeholder="react, backend"
    )

    locations = st.sidebar.multiselect(
        "Locations",
        ["remote", "usa", "europe", "india", "uk"],
        default=[]
    )

    job_types = st.sidebar.multiselect(
        "Job Type",
        ["full-time", "part-time", "contract", "internship"],
        default=[]
    )

    sources = st.sidebar.multiselect(
        "Sources",
        ["remoteok", "remotive", "arbeitnow"],
        default=[]
    )

    remote_only = st.sidebar.checkbox("Remote Only")

    posted_within = st.sidebar.selectbox(
        "Posted Within",
        ["Any", "24 hours", "3 days", "7 days", "30 days"]
    )

    def split_values(value):
        return [v.strip().lower() for v in value.split(",") if v.strip()] if value else []

    filters = {
        "provider": provider,
        "keywords": split_values(keywords),
        "locations": [l.lower() for l in locations],
        "job_types": [j.lower() for j in job_types],
        "sources": [s.lower() for s in sources],
        "remote_only": remote_only,
        "posted_within": None if posted_within == "Any" else posted_within,
    }

    search_clicked = st.sidebar.button("Search Jobs")

    return filters, search_clicked