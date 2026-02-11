from bi_logic import pipeline_by_sector, revenue_this_quarter
from monday_client import fetch_board, WORK_BOARD_ID, DEALS_BOARD_ID
from data_processor import clean_board_data

# Load fresh data each query (real BI style)

def load_data():
    work_raw = fetch_board(WORK_BOARD_ID)
    deals_raw = fetch_board(DEALS_BOARD_ID)

    work_df = clean_board_data(work_raw)
    deals_df = clean_board_data(deals_raw)

    return work_df, deals_df


def handle_query(user_query):
    q = user_query.lower()

    work_df, deals_df = load_data()

    # --- Pipeline queries ---
    if "pipeline" in q:
        if "mining" in q:
            return pipeline_by_sector(deals_df, "Mining")
        if "power" in q or "powerline" in q:
            return pipeline_by_sector(deals_df, "Powerline")

        return "Which sector should I analyze? (Mining, Powerline, Renewables)"

    # --- Revenue queries ---
    if "revenue" in q and "quarter" in q:
        return f"Revenue this quarter: {revenue_this_quarter(work_df)}"

    if "revenue" in q:
        return f"Total revenue: {work_df['revenue'].sum()}"

    return "I can help with pipeline, revenue, and sector performance. Try asking differently."
