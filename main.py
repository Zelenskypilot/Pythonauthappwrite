from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from appwrite.client import Client
from appwrite.services.account import Account
from fastapi.responses import JSONResponse

# Initialize FastAPI app
app = FastAPI()

# Initialize Appwrite Client
client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1')  # Appwrite Base URL
client.set_project('6765e2280022c08ed121')  # Your Project ID
client.set_key('standard_a33daf76dd1ac64a8dffac5ecc7b7572f669114e140df3af6add28391712ea5a9e6c0d29476b5aaf07c604e43aecfaa133a2a919a46c73b965545609004e973a164c4aae1d0be3a9707bb9ca1a085e9afe61b1d047abc7ff3a0a9ca705fb68e100535fe55fe17286c2a3367c90c3d0c033857d0c79b524094bd5b829bb5e7570')  # Your API Key

# Pydantic models for request bodies
class LoginRequest(BaseModel):
    email: str
    password: str

class SignupRequest(BaseModel):
    email: str
    password: str
    name: str

@app.post("/login")
async def login(request: LoginRequest):
    account = Account(client)
    try:
        session = account.create_session(email=request.email, password=request.password)
        return JSONResponse(content={"message": "Login successful", "session": session}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Login failed: {str(e)}")

@app.post("/signup")
async def signup(request: SignupRequest):
    account = Account(client)
    try:
        user = account.create(email=request.email, password=request.password, name=request.name)
        return JSONResponse(content={"message": "Signup successful", "user": user}, status_code=201)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Signup failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
