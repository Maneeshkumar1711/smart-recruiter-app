from fastapi import FastAPI
from app.routes import user_routes, role_routes, user_role_routes

app = FastAPI(title="Smart Recruitment App")

app.include_router(user_routes.router)
app.include_router(role_routes.router)
app.include_router(user_role_routes.router)

@app.get("/")
def root():
    return {"message": "Backend running 🚀"}
