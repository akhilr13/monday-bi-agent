from bi_logic import (
    pipeline_by_sector,
    revenue_this_quarter,
    best_sector,
    data_quality
)


# -----------------------------
# Smart explanation layer
# -----------------------------

def explain_revenue(value, df):
    zero_or_missing = (df["revenue"].isna().sum() + (df["revenue"] == 0).sum())

    if value == 0:
        return f"""
Revenue this quarter is ₹0.

Key observations:
• Most work orders are scheduled in future periods
• {zero_or_missing} records have missing or zero revenue values

This likely understates true business performance.
"""
    else:
        return f"Revenue this quarter is ₹{round(value,2)}"


def explain_pipeline(result):
    if result["deal_count"] == 0:
        return f"""
No active deals found in the {result['sector']} sector.

This may indicate:
• Deals not tagged with sector properly
• Pipeline currently inactive
"""

    return f"""
Pipeline summary for {result['sector']} sector:

• Active deals: {result['deal_count']}
• Total pipeline value: ₹{result['total_pipeline_value']}
"""


# -----------------------------
# Main query handler
# -----------------------------

def handle_query(query, work_df, deals_df):

    q = query.lower()

    # -------- Revenue --------
    if "revenue" in q and "quarter" in q:
        revenue = revenue_this_quarter(work_df)
        return explain_revenue(revenue, work_df)

    # -------- Pipeline sector --------
    if "pipeline" in q and "sector" in q:
        for sector in deals_df["sector"].dropna().unique():
            if sector.lower() in q:
                result = pipeline_by_sector(deals_df, sector)
                return explain_pipeline(result)

        return "Which sector would you like to analyze?"

    if "pipeline" in q:
        return "Please specify the sector (for example: mining pipeline)"

    # -------- Best sector --------
    if "best sector" in q or "top sector" in q:
        sector_perf = best_sector(work_df)

        if sector_perf is None:
            return "Not enough data to evaluate sector performance."

        best = sector_perf.index[0]
        value = sector_perf.iloc[0]

        return f"Best performing sector is {best} with ₹{round(value,2)} revenue."

    # -------- Data quality --------
    if "data quality" in q or "missing" in q:
        work_report = data_quality(work_df)
        deals_report = data_quality(deals_df)

        return {
            "work_orders": work_report,
            "deals": deals_report
        }

    # -------- Help fallback --------
    return """
I can help with:

• Revenue this quarter
• Pipeline by sector (example: mining pipeline)
• Best performing sector
• Data quality issues

Try asking one of these.
"""
