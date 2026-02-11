from agent import handle_query

while True:
    q = input("Founder: ")
    print("Agent:", handle_query(q))
