from fastapi import FastAPI, HTTPException, status
from database import init_db, create_user, get_user
from schemas import UserCreate, UserResponse
import sqlite3
from contextlib import asynccontextmanager

# A **lifespan** **handler** lets you define code that runs 
# **right before the server starts accepting requests**, and right after it shuts down:

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    init_db()
    yield # The application runs while waiting here
    
    print("Application shutting down...")

app = FastAPI(lifespan=lifespan)


@app.post("/users", response_model = UserResponse, status_code = status.HTTP_201_CREATED) # this ensures that newly created row matches the resource
def add_user(user: UserCreate):
    try:
        create_user(user.username, user.token_limit)
        return get_user(user.username)
    except sqlite3.IntegrityError:
        raise HTTPException(status_code= 409, detail = "Username already exists")
    # should this return something, or just execute the query?
    # yes a status code to signal that change was committed successfully

@app.get("/users/{username}", response_model = UserResponse) # usingh response model ensures that only what is necessary is returned
# to the client to safely guard sensitive columns of the db
def find_user(username:str):
    row = get_user(username) # string should be passed directly or python considers it a "set"
    
    if not row:
        raise HTTPException(status_code= 404, detail = "Username not found!")
    
    return row