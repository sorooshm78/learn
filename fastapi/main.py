from fastapi import FastAPI

app = FastAPI()


@app.get("/h")
async def root():
    return {"message": "Hello World"}


# uvicorn main:app --reload
# The command uvicorn main:app refers to:

#     main: the file main.py (the Python "module").
#     app: the object created inside of main.py with the line app = FastAPI().
#     --reload: make the server restart after code changes. Only use for development.

# # --------------------------------------
