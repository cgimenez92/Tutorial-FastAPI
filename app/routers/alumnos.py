from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, dal
from app.database import get_db

router = APIRouter(
    prefix="/alumnos",
    tags=["alumnos"]
)

@router.post("/", response_model=schemas.AlumnoResponse)
async def crear(alumno: schemas.AlumnoCreateRequest, db: AsyncSession = Depends(get_db)):
    return await dal.crear_alumno(db, alumno)
