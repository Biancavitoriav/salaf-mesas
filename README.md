# SalaF Mesas — Automated Classroom Seating

A Python/Flask web application that automates daily random seating rotation for **24 students** across **5 tables** in a real classroom at **Instituto J&F** (2nd year F, 2024).

## Problem

Teachers needed a fair, unbiased way to reshuffle student groups ("panelinhas") every day to improve focus and classroom dynamics. As class representative, I built a transparent automated solution to replace manual seating decisions.

## Features

- **Daily random shuffle:** Distributes 24 registered students evenly across 5 tables
- **Scheduled automation:** Uses `APScheduler` to run the rotation every day at **6:00 AM** (America/Sao_Paulo)
- **Live classroom layout:** Web UI renders the physical room layout with CSS Grid — board, aisle, teacher desk, and table positions

## Tech Stack

- **Python 3** + **Flask** — web routes and template rendering
- **APScheduler** — background cron-style job scheduling
- **pytz** — timezone handling (Brasília)
- **HTML5 & CSS3** — responsive layout with CSS Grid and Flexbox

## Installation

```bash
git clone https://github.com/Biancavitoriav/salaf-mesas.git
cd salaf-mesas
pip install -r requirements.txt
python app.py
```

## Dependencies

    Flask==2.2.5
    APScheduler==3.10.1
    pytz==2023.3

## Impact

- Used daily in a real classroom throughout 2024
- Saved teachers ~15 minutes per day on manual seating
- Eliminated bias in group formation with 100% random, auditable rotation

## Author

[@Biancavitoriav](https://github.com/Biancavitoriav) — Instituto J&F
