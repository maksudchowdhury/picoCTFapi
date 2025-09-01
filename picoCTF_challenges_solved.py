import requests
import csv

# ------------------------------
# Session info
# ------------------------------
cookies = {
    "csrftoken": "<your token>",
    "sessionid": "<your token>",
}
headers = {
    "x-csrftoken": "<your token>",
    "accept": "application/json"
}

# ------------------------------
# CSV setup
# ------------------------------
csv_file = "picoCTF_solved_challenges.csv"
fieldnames = ["Name", "Category", "difficulty", "status", "Problem Existance"]

# ------------------------------
# Pagination loop
# ------------------------------
page = 1
solved_challenges = []

while True:
    url = f"https://play.picoctf.org/api/challenges/?page_size=100&page={page}"
    response = requests.get(url, cookies=cookies, headers=headers)
    data = response.json()

    for challenge in data["results"]:
        if challenge.get("solved_by_user"):
            solved_challenges.append({
                "Name": challenge["name"],
                "Category": challenge["category"]["name"] if challenge.get("category") else "Unknown",
                "difficulty": challenge.get("difficulty", ""),
                "status": "Solved",
                "Problem Existance": "Exists" if not challenge.get("retired") else "Retired"
            })

    if not data.get("next"):
        break
    page += 1

# ------------------------------
# Write to CSV
# ------------------------------
with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(solved_challenges)

print(f"✅ CSV file created: {csv_file} ({len(solved_challenges)} solved challenges)")
