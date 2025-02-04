from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from routers.math_route import router as math_router


app = FastAPI()

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allows all origin
    allow_credentials=True,
    allow_methods=["GET"],
)

app.include_router(math_router)

@app.get("/")
async def root():
    return JSONResponse(content={"message": "Welcome to the Math API!"})