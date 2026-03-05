import streamlit as st

def render_results(jobs):

    if not jobs:
        st.warning("⚠ No jobs found matching the selected filters.")
        return

    st.subheader(f"Jobs Found: {len(jobs)}")

    for job in jobs:

        with st.container():

            st.markdown(f"### {job.get('title') or '-'}")

            st.write(f"Company: {job.get('company') or '-'}")

            st.write(f"Location: {job.get('location') or '-'}")

            st.write(f"Source: {job.get('source') or '-'}")

            if job.get("url"):
                st.markdown(f"[Apply Here]({job['url']})")
            else:
                st.write("Apply Link: -")

            st.divider()
