from fastapi import FastAPI, Form
from pydantic import BaseModel
from appwrite.client import Client
from appwrite.services.account import Account
from fastapi.responses import JSONResponse

app = FastAPI()

# Initialize Appwrite Client
client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1')  # Appwrite Base URL
client.set_project('6765e2280022c08ed121')  # Your Project ID
client.set_key('standard_a33daf76dd1ac64a8dffac5ecc7b7572f669114e140df3af6add28391712ea5a9e6c0d29476b5aaf07c604e43aecfaa133a2a919a46c73b965545609004e973a164c4aae1d0be3a9707bb9ca1a085e9afe61b1d047abc7ff3a0a9ca705fb68e100535fe55fe17286c2a3367c90c3d0c033857d0c79b524094bd5b829bb5e7570')

# Define request models for signup and login
class User(BaseModel):
    email: str
    password: str
    name: str = None

@app.post("/login")
async def login(user: User):
    account = Account(client)
    try:
        session = account.create_session(email=user.email, password=user.password)
        return JSONResponse(content={"message": "Login successful", "session": session}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)

@app.post("/signup")
async def signup(user: User):
    account = Account(client)
    try:
        new_user = account.create(email=user.email, password=user.password, name=user.name)
        return JSONResponse(content={"message": "Signup successful", "user": new_user}, status_code=201)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
