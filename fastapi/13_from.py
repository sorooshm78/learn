from typing import Annotated

from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}


# About "Form Fields"
# The way HTML forms (<form></form>) sends the data to the server normally uses a "special" encoding for that data, it's different from JSON.
# FastAPI will make sure to read that data from the right place instead of JSON.
# Technical Details
# Data from forms is normally encoded using the "media type" application/x-www-form-urlencoded.
# But when the form includes files, it is encoded as multipart/form-data. You'll read about handling files in the next chapter.
# If you want to read more about these encodings and form fields
