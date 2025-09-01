# picoCTF Challenges Exporter

This repository contains Python scripts to export your **picoCTF challenges** into a CSV file.  

picoCTF does **not provide an easy way to see which challenges you solved separately**, so these scripts allow you to generate a local CSV file for better tracking, sorting, and analysis.

---

## 📂 Repository Structure

- `picoCTF_challenges_all.py` – Exports **all challenges** (solved and unsolved) into a CSV.
- `picoCTF_challenges_solved.py` – Exports **only the solved challenges** into a CSV.

---

## 🔹 Why this program exists

picoCTF’s official website shows challenges in a paginated format and does not allow users to filter or download solved challenges separately. These scripts solve that problem by:

1. Fetching all challenges from the picoCTF API.
2. Filtering solved challenges if required.
3. Exporting the data to a CSV with key information:  
   - **Name** – Challenge name  
   - **Category** – Challenge category (e.g., Forensics, Web Exploitation)  
   - **Difficulty** – Difficulty level  
   - **Status** – Solved / Unsolved  
   - **Problem Existence** – Exists / Retired  

This allows students to **track their progress**, **analyze solved challenges**, or **plan their learning** efficiently.

---

## 🔹 Prerequisites

- Python 3.x installed
- Modules: `requests` (install via `pip install requests`)
- CSV files are generated automatically in the same folder as the script.

---

## 🔹 How to get your credentials (Cookies & Headers)

1. Log in to [picoCTF](https://play.picoctf.org) using your browser.
2. Open **Developer Tools**:
   - Chrome: `Ctrl + Shift + I` → Network tab
   - Firefox: `Ctrl + Shift + E`
3. Go to the **Network tab**, then reload the page.
4. Click any request to `/api/challenges/` in the list.
5. Under **Headers**, copy:
   - **Cookie header** – looks like:  
     ```
     csrftoken=xxxx; sessionid=xxxx; ...
     ```
   - **x-csrftoken** value from request headers.
6. Replace these values in the script:

```python
cookies = {
    "csrftoken": "YOUR_CSRF_TOKEN_HERE",
    "sessionid": "YOUR_SESSIONID_HERE",
}
headers = {
    "x-csrftoken": "YOUR_CSRF_TOKEN_HERE",
    "accept": "application/json"
}
```

## 🔹 Script Usage

### 1. Export all challenges
```bash
python picoCTF_challenges_all.py
```
- Fetches **all challenges** (solved and unsolved).
- Creates `picoCTF_challenges_all.csv` with the following columns:  
  `Name, Category, difficulty, status, Problem Existence`.

### 2. Export only solved challenges
```bash
python picoCTF_challenges_solved.py
```
- Fetches **only solved challenges**.
- Creates `picoCTF_solved_challenges.csv` with the same columns.

---

## 🔹 How it works

1. **Pagination**  
   - The picoCTF API returns challenges in pages (`page_size=100`).
   - Scripts loop through pages until there are no more (`next=null`).

2. **Data Extraction**  
   - `Name` → `challenge["name"]`  
   - `Category` → `challenge["category"]["name"]`  
   - `difficulty` → `challenge["difficulty"]`  
   - `status` → `"Solved"` / `"Unsolved"` based on `challenge["solved_by_user"]`  
   - `Problem Existence` → `"Exists"` / `"Retired"` based on `challenge["retired"]`

3. **CSV Export**  
   - Uses Python’s `csv.DictWriter` to write headers and rows.

4. **Filtering solved challenges**  
   - The solved-only script filters challenges where `solved_by_user == True`.

---

## 🔹 Guidelines / Tips

- Make sure your **cookies are valid**; otherwise, API requests will fail.
- Keep your `csrftoken` and `sessionid` private. Do **not** share publicly.
- Open the resulting CSV in Excel, Google Sheets, or any spreadsheet software for sorting/filtering.

---

## 🔹 Example Output

| Name         | Category           | difficulty | status  | Problem Existence |
|-------------|------------------|------------|---------|-----------------|
| DISKO 1      | Forensics         | 1          | Solved  | Exists          |
| SSTI1        | Web Exploitation  | 1          | Unsolved| Exists          |
| hashcrack    | Cryptography      | 1          | Solved  | Exists          |
