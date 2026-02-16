# Swap Numbers API

Do numbers swap karne wala simple API (FastAPI).

## Local run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Tests

```bash
pytest tests/ -v
```

## Auto Test → Branch → PR (GitHub Actions)

Jab bhi tum **push** karoge (GitHub par):

1. **Pehle tests chalenge** – koi error nahi honi chahiye.
2. **Agar tests pass:**
   - **Feature branch** par push kiya hai → usi branch ke liye **PR khul jayega** (main ki taraf).
   - **Main** par push kiya hai → **nayi branch** `ready/auto-<run_id>` banegi, push hogi, aur us branch ke liye **PR** create ho jayega.

Yani: tum (ya AI) bas push karo – testing khud hogi, pass hone par branch/PR flow automatic.
