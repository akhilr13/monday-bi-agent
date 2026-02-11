import pandas as pd

def clean_board_data(raw_items):
    rows = []

    for item in raw_items:
        row = {}

        # Always keep item name
        row["project"] = item.get("item_name")

        for key, value in item.items():
            if key == "item_name":
                continue

            # Smart mapping based on content
            if "status" in key:
                row["status"] = value

            elif "date" in key:
                row["end_date"] = value

            elif "number" in key or "numbers" in key:
                try:
                    row["revenue"] = float(value)
                except:
                    row["revenue"] = 0

            elif "color" in key:
                row["sector"] = value

            elif "text" in key:
                row["client"] = value

        rows.append(row)

    return pd.DataFrame(rows)
