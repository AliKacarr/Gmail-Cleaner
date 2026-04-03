def build_query():
    with open("filterFrom.txt", "r") as f:
        addresses = [line.strip() for line in f.readlines() if line.strip()]

    query_parts = []
    for address in addresses:
        query_parts.append(f"(from:{address} OR to:{address})")

    return " OR ".join(query_parts)
