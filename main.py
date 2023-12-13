from fastapi import FastAPI
from tags import tags_metadata
from routers import api_router

app = FastAPI(title='PowerAI - Local AIs all in one place', openapi_tags=tags_metadata)
app.include_router(api_router.api_router)


@app.get("/welcome", description="Welcome to PowerAI", name="Welcome")
async def root():
    return {"message": "Hello World"}


@app.get("/setup/{username}")
async def say_hello(username: str):
    return {"message": f"Hello {username}"}
