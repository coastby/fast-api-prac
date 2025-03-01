from fastapi import FastAPI
from controller.items import router as items_router
from controller.users import router as users_router
from controller.admins import router as admins_router

app = FastAPI()

app.include_router(items_router)
app.include_router(users_router)
app.include_router(admins_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
  
