import pandas as pd
from datetime import datetime

def pipeline_by_sector(deals_df, sector_name):
    filtered = deals_df[deals_df["sector"] == sector_name]

    if "revenue" in filtered.columns:
        total_revenue = filtered["revenue"].sum()
    else:
        total_revenue = 0   # Deals board has no revenue

    deal_count = len(filtered)

    return {
        "sector": sector_name,
        "deal_count": deal_count,
        "total_pipeline_value": total_revenue
    }



def revenue_this_quarter(df):
    df["end_date"] = pd.to_datetime(df["end_date"], errors="coerce")

    current_q = pd.Timestamp.now().quarter
    current_year = pd.Timestamp.now().year

    quarter_df = df[
        (df["end_date"].dt.quarter == current_q) &
        (df["end_date"].dt.year == current_year)
    ]

    return quarter_df["revenue"].sum()
