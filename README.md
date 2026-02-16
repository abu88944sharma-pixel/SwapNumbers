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

1. **🤖 AI automatically tests generate karega** – codebase analyze karke comprehensive test cases banayega
2. **✅ Pehle tests chalenge** – koi error nahi honi chahiye
3. **Agar tests pass:**
   - **Feature branch** par push kiya hai → usi branch ke liye **PR khul jayega** (main ki taraf)
   - **Main** par push kiya hai → **nayi branch** (`first_branch`, `second_branch`, etc.) banegi, push hogi, aur us branch ke liye **PR** create ho jayega

**Setup (ek baar):**
1. GitHub repo → **Settings → Secrets and variables → Actions**
2. **New repository secret** → Name: `OPENAI_API_KEY`, Value: apna OpenAI API key
3. Done! Ab har push par AI tests generate karega

**Note:** Agar `OPENAI_API_KEY` set nahi hai, to manual tests use honge (backward compatible).

Yani: tum (ya AI) bas push karo – **AI tests generate karega**, testing khud hogi, pass hone par branch/PR flow automatic.
