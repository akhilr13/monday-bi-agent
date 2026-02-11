import requests

# ==========================
# CONFIG
# ==========================

MONDAY_API_URL = "https://api.monday.com/v2"

MONDAY_API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjYxOTg0Mjk1NiwiYWFpIjoxMSwidWlkIjo5OTcwNTE5MSwiaWFkIjoiMjAyNi0wMi0xMVQwNjo1NTo1OS42MzdaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MzM3NDgyMTAsInJnbiI6ImFwc2UyIn0.K7CV_h8HxBCtFHmUcLfV4UFNj8jZNmg0GDuMlYstNIc"

HEADERS = {
    "Authorization": MONDAY_API_KEY,
    "Content-Type": "application/json"
}

# Optional – you can set defaults if you want
WORK_BOARD_ID = 5026562796
DEALS_BOARD_ID = 5026563840


# ==========================
# CORE FETCH FUNCTION
# ==========================

def fetch_board(board_id):
    query = f"""
    {{
      boards(ids: {board_id}) {{
        items_page {{
          items {{
            id
            name
            column_values {{
              id
              text
            }}
          }}
        }}
      }}
    }}
    """

    response = requests.post(
        MONDAY_API_URL,
        json={"query": query},
        headers=HEADERS
    )

    if response.status_code != 200:
        raise Exception(f"API Error: {response.text}")

    data = response.json()

    return extract_items(data)


# ==========================
# CLEAN RESPONSE → PYTHON LIST
# ==========================

def extract_items(response_json):
    boards = response_json["data"]["boards"]
    rows = []

    for board in boards:
        for item in board["items_page"]["items"]:
            row = {"item_name": item["name"]}

            for col in item["column_values"]:
                row[col["id"]] = col["text"]

            rows.append(row)

    return rows


# ==========================
# QUICK TEST
# ==========================

if __name__ == "__main__":
    TEST_BOARD_ID = 123456789   # replace with real board id
    rows = fetch_board(TEST_BOARD_ID)

    for r in rows[:5]:
        print(r)
