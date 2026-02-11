from monday_client import fetch_board, WORK_BOARD_ID, DEALS_BOARD_ID
from data_processor import clean_board_data
from bi_logic import pipeline_by_sector, revenue_this_quarter

# -------- Fetch boards --------

work_raw = fetch_board(WORK_BOARD_ID)
deals_raw = fetch_board(DEALS_BOARD_ID)

# -------- Clean data --------

work_df = clean_board_data(work_raw)
deals_df = clean_board_data(deals_raw)

print("WORK DATA:")
print(work_df.head())

print("\nDEALS DATA:")
print(deals_df.head())

# -------- BI Intelligence --------

energy_pipeline = pipeline_by_sector(deals_df, "Mining")

print("\nMining Pipeline:")
print(energy_pipeline)

print("\nRevenue this quarter (Work Orders):")
print(revenue_this_quarter(work_df))
