# Retail Orders ETL

A small ETL pipeline built with Python and Pandas to clean and validate retail order data.

## Status

Day 1 of 4: data cleaning and validation completed.

## What it does

1. Reads raw order data from `orders.csv`
2. Removes exact duplicate rows
3. Converts order dates to a proper date format
4. Flags invalid rows:
   - Missing amount
   - Invalid date
   - Negative amount
5. Saves valid rows to `clean_orders.csv` and invalid rows to `rejected_orders.csv`

## Why rejected rows are saved

Bad rows are kept in a separate file instead of being deleted, so they can be checked and fixed later.

## Tech used

- Python
- Pandas

## How to run

```bash
pip install pandas
python clean_orders.py
```

## Planned next steps

- Load clean data into a SQLite database
- Write SQL queries for business questions
- Add logging