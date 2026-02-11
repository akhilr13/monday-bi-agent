import streamlit as st

from monday_client import fetch_board, WORK_BOARD_ID, DEALS_BOARD_ID
from data_processor import clean_board_data
from agent import handle_query


st.set_page_config(page_title="Monday BI Agent", layout="centered")

st.title("📊 Monday.com Business Intelligence Agent")
st.write("Ask founder-level business questions:")

query = st.text_input("Your question:")

@st.cache_data
def load_data():
    work_raw = fetch_board(WORK_BOARD_ID)
    deals_raw = fetch_board(DEALS_BOARD_ID)

    work_df = clean_board_data(work_raw)
    deals_df = clean_board_data(deals_raw)

    return work_df, deals_df


work_df, deals_df = load_data()

if query:
    answer = handle_query(query, work_df, deals_df)
    st.success(answer)
