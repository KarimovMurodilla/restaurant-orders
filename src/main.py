import uvicorn
from fastapi import FastAPI

from api.routers import all_routers
from db.mongodb import MongoDBManager

app = FastAPI(
    title="Restaurant Orders"
)


for router in all_routers:
    if isinstance(router, dict):
        app.include_router(**router)

    else:
        app.include_router(router)


@app.on_event("startup")
async def startup_db_client():
    mongodb_url = "mongodb://sweet:sweet@localhost:27017"
    db_name = "restaurants"
    await MongoDBManager.connect_to_mongodb(mongodb_url, db_name)


@app.on_event("shutdown")
async def shutdown_db_client():
    await MongoDBManager.close_mongodb_connection()


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)