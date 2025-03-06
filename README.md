### Get started 
---
1. Dependencies install: 

        `pip install -r requirements.txt`

2. Create a .env file:

        `DATABASE_URL="sqlite:///{path}"`

3. Run uvicorn server: 

        `uvicorn src.api:app --reload`
---