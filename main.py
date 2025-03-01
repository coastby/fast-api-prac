from fastapi import FastAPI
from controller.items import router as items_router

app = FastAPI()

app.include_router(items_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
  
