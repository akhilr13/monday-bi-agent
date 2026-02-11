import streamlit as st
from agent import handle_query

st.set_page_config(page_title="Monday BI Agent", layout="centered")

st.title("📊 Monday.com Business Intelligence Agent")

st.write("Ask founder-level business questions:")

query = st.text_input("Your question:")

if query:
    with st.spinner("Analyzing live data..."):
        answer = handle_query(query)
    st.success(answer)
