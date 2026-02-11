import pandas as pd

# -----------------------------
# Pipeline by sector
# -----------------------------

def pipeline_by_sector(deals_df, sector_name):
    if "sector" not in deals_df.columns:
        return {"error": "Sector data missing in deals board"}

    filtered = deals_df[deals_df["sector"] == sector_name]

    if filtered.empty:
        return {
            "sector": sector_name,
            "deal_count": 0,
            "total_pipeline_value": 0
        }

    if "revenue" not in filtered.columns:
        total_value = 0
    else:
        total_value = filtered["revenue"].fillna(0).sum()

    return {
        "sector": sector_name,
        "deal_count": len(filtered),
        "total_pipeline_value": round(float(total_value), 2)
    }


# -----------------------------
# Revenue this quarter
# -----------------------------

def revenue_this_quarter(work_df):
    if "end_date" not in work_df.columns or "revenue" not in work_df.columns:
        return 0

    work_df["end_date"] = pd.to_datetime(work_df["end_date"], errors="coerce")

    now = pd.Timestamp.now()
    q = now.quarter
    y = now.year

    q_df = work_df[
        (work_df["end_date"].dt.quarter == q) &
        (work_df["end_date"].dt.year == y)
    ]

    return float(q_df["revenue"].fillna(0).sum())


# -----------------------------
# Best performing sector
# -----------------------------

def best_sector(work_df):
    if "sector" not in work_df.columns or "revenue" not in work_df.columns:
        return None

    sector_perf = (
        work_df.groupby("sector")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    if sector_perf.empty:
        return None

    return sector_perf


# -----------------------------
# Data quality report
# -----------------------------

def data_quality(df):
    report = {}

    for col in df.columns:
        report[col] = {
            "missing": int(df[col].isna().sum()),
            "total": int(len(df))
        }

    return report
