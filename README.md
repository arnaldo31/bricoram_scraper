
# Bricoram Scraper (Python + SeleniumBase + SQLAlchemy)

This project scrapes professional profile data from bricoram.com and stores it into a SQLite database (.db) and Excel file (.xlsx). It extracts profiles, reviews, images, and prices in a structured relational format.

All data is stored in 4 tables:
profiles, reviews, images, prices

Each field includes a meaning description.

---

# INSTALLATION

## 1. Install Python

Download Python 3.10+:
https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe

IMPORTANT:
✔ Check "Add Python to PATH"

Verify:
python --version
pip --version

---

## 2. Open Command Prompt (CMD)

Before installing anything:
- Press Windows + R
- Type: cmd
- Press Enter

Run all commands inside CMD.

---

## 3. Install Libraries (one by one)

pip install seleniumbase  
→ Browser automation (SeleniumBase)

pip install beautifulsoup4  
→ HTML parsing (BeautifulSoup)

pip install pandas  
→ Data handling + Excel export

pip install sqlalchemy  
→ Database ORM (SQLite handling)

pip install openpyxl  
→ Excel file writer engine

---

## OR install everything at once:
pip install seleniumbase beautifulsoup4 pandas sqlalchemy openpyxl

---

# PROJECT STRUCTURE

```text
bricoram-scraper/
├── scraper.py
├── save/
│   ├── bricoram.db
│   └── bricoram_save.xlsx
└── README.md
```
---

# HOW TO RUN

python scraper.py

---

# DATABASE SETUP

import os
from sqlalchemy import create_engine

os.makedirs("save", exist_ok=True)

engine = create_engine(
    "sqlite:///save/bricoram.db",
    echo=False
)

---

# 🗄 DATABASE SCHEMA (TABLE FORMAT)

---

## 📌 TABLE: profiles

| Column | Type | Meaning |
|--------|------|--------|
| id | INTEGER (PK) | Unique profile ID |
| category | TEXT | Service category type |
| name | TEXT | Business or professional name |
| intro_message | TEXT | Short introduction message |
| about | TEXT | Full description of profile |
| city_region | TEXT | City or region location |
| email | TEXT | Contact email address |
| instagram | TEXT | Instagram profile link |
| tiktok | TEXT | TikTok profile link |
| youtube | TEXT | YouTube channel link |
| linkedin | TEXT | LinkedIn profile link |
| location | TEXT | Physical address |
| phone | TEXT | Phone number |
| reviews_count | INTEGER | Total number of reviews |
| reviews_average | FLOAT | Average rating score |
| services | TEXT | List of services offered |
| profile_image | TEXT | Main profile image URL |
| website | TEXT | Official website URL |

---

## 📌 TABLE: reviews

| Column | Type | Meaning |
|--------|------|--------|
| id | INTEGER (PK, AUTOINCREMENT) | Unique review record ID |
| profile_id | INTEGER | Linked profile ID |
| client_name | TEXT | Name of reviewer |
| date | TEXT | Review date |
| rating | FLOAT | Rating score (1–5) |
| text | TEXT | Review content |

---

## 📌 TABLE: images

| Column | Type | Meaning |
|--------|------|--------|
| id | INTEGER (PK, AUTOINCREMENT) | Unique image record ID |
| profile_id | INTEGER | Linked profile ID |
| image_link | TEXT | Image URL (portfolio / achievements) |

---

## 📌 TABLE: prices

| Column | Type | Meaning |
|--------|------|--------|
| id | INTEGER (PK, AUTOINCREMENT) | Unique price record ID |
| profile_id | INTEGER | Linked profile ID |
| title | TEXT | Service name |
| unit | TEXT | Unit type (hour, project, etc.) |
| value | FLOAT | Price value |

---

# 📊 EXCEL OUTPUT

save/bricoram_save.xlsx

Sheets:
- Details → profiles
- Reviews → reviews
- Images → images
- Prices → prices

---

# 🔄 DATA FLOW

API Requests → SeleniumBase Scraping → JSON Parsing → SQLite Insert → Excel Export

---

# 💻 CORE INSERT LOGIC

session.add(Profile(...))
session.commit()

for r in reviews:
    session.add(Review(
        profile_id=id,
        client_name=r["client_name"],
        date=r["date"],
        rating=r["rating"],
        text=r["text"]
    ))
    session.commit()

for img in images:
    session.add(Image(
        profile_id=id,
        image_link=img["imageLink"]
    ))
    session.commit()

for p in prices:
    session.add(Price(
        profile_id=id,
        title=p["title"],
        unit=p["unit"],
        value=p["value"]
    ))
    session.commit()

---

# ⚡ FEATURES

✔ Real-time database insertion  
✔ Multi-table relational structure  
✔ SQLite storage (.db)  
✔ Excel export (.xlsx)  
✔ Crash-safe scraping  
✔ Structured ETL pipeline  

---

# ⚠️ IMPORTANT NOTES

- Always create `save/` folder before running
- Run all pip commands inside CMD
- Use `profile_id` to link tables correctly
- Always use `session.commit()` after inserts
- Use rollback on errors
- Avoid duplicate scraping using ID tracking

---


# 👨‍💻 AUTHOR

Built using:
Python, SeleniumBase, BeautifulSoup, SQLAlchemy, Pandas
