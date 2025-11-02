from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.base import Base
from app.database.session import async_engine, async_session
from app.api.v1 import router as api_router

# -------------------------------
# Lifespan pour startup / shutdown
# -------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: création des tables
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Application démarrée")
    print("🔗 Swagger UI: http://localhost:8000/docs")
    
    yield  # Exécution normale de l'application
    
    # Shutdown
    print("🛑 Application arrêtée")

# -------------------------------
# Application FastAPI
# -------------------------------
app = FastAPI(
    title="SoilAdvisor API",
    version="1.0.0",
    description="API pour la gestion des parcelles, analyses de sol et images satellite",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# -------------------------------
# CORS
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Inclusion des routers
# -------------------------------
app.include_router(api_router.router, prefix="/api/v1")

# -------------------------------
# Endpoint santé
# -------------------------------
@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "API en bonne santé", "version": "1.0.0"}

# -------------------------------
# Dépendance AsyncSession
# -------------------------------
async def get_db():
    async with async_session() as session:
        yield session

# -------------------------------
# Lancement du serveur
# -------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
