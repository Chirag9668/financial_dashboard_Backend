# Finance Dashboard Backend

This is a backend project I made for managing financial records like income and expense and showing summary on dashboard.

The idea is not to build bank system but to track financial activities and show insights like how much earned and how much spent.

---

## Tech used

* FastAPI
* SQLite
* SQLAlchemy

---

## Features

* User creation with roles (admin, analyst, viewer)
* Add income and expense records
* Get all records
* Delete records
* Dashboard summary (income, expense, balance)
* Category wise breakdown
* Recent activity
* Batch record insert (multiple records at once)

---

## How it works

User first gets created, then he can add financial entries like income or expense.
System stores all records and calculates summary based on that.

Important: This system does not track actual bank balance, it only shows financial data based on user entries.

---

## API Flow (basic)

1. Create user
2. Add income
3. Add expense
4. Get dashboard summary
5. Get category breakdown
6. Get recent activity

---

## Example

Income = 10000
Expense = 100

Then dashboard will show:

income: 10000
expense: 100
balance: 9900

Even if expense is more than income it can go negative, which means overspending.

---

## Roles

* Admin → can create, delete records
* Analyst → can view data and dashboard
* Viewer → limited access

---

## Setup

Run this command:

uvicorn app.main:app --reload

Then open:

http://127.0.0.1:8000/docs

---

## Notes

* Used simple SQLite for storage
* Focus was on backend logic and structure
* Some improvements can be added like authentication and pagination

---

## Final

I tried to keep the system simple but logical, focusing on how backend actually works instead of making it too complex.

---
"# financial_dashboard_Backend" 
