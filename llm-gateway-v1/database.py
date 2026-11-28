## IN database we don't raise any error that is handled in main, this is purely SQL and database handling file
from pydantic import BaseModel, Field
import sqlite3


def connect_help(db_path: str = "app_data.db") -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(db_path: str = "app_data.db"):
    with connect_help(db_path) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users(
            username TEXT PRIMARY KEY,
            token_limit INTEGER NOT NULL
            )
            """
        )
    conn.close()

def create_user(username: str, token_limit: int): ## params should be passed not as a class in this file. don't use class
    with connect_help() as conn:   
        conn.execute(
            "INSERT INTO users (username, token_limit) VALUES (?,?)", ## passing the params should be out of ""
            (username, token_limit)   
        )

def get_user(username:str):
    with connect_help() as conn:   
        row = conn.execute(
            "SELECT username, token_limit FROM users where username = ?",
            (username,) # if this is not a tuple python will treat it as string and pass it as individual letters
        ).fetchone()
        if row is None: return None
        return {"username": row["username"], "token_limit": row["token_limit"]}