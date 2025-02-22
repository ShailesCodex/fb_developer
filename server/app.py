from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.endpoints.fb_dev import camp_router

async def app_startup():
    try:
        pass
        # init_db()
    except Exception as e:
        # TODO: log error
        print(e)

async def lifespan(app: FastAPI):
    await app_startup()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(camp_router, prefix="/v1")


app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_headers=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
)


@app.get("/")
async def welcome():
    return {"status": 200, "message": "Server running"}
