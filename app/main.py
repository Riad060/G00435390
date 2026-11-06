from fastapi import (Depends, FastAPI, HTTPException, status, )
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.database import engine, get_db
from app.models import Base,MaintenanceDB
from app.schemas import(MaintenanceCreate, MaintenanceRead)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Example template")

@app.get("/health")
def health():
    return{"status": "ok"}

@app.post(
    "/api/maintenances",
    response_model=MaintenanceRead,
    status_code=201,
)
def create_maintenance(
    new_maintenance:MaintenanceCreate,
    db:Session=Depends(get_db),
):
    db_maintenance=MaintenanceDB(
        **new_maintenance.model_dump()
    )
    db.add(db_maintenance)
    try:
        db.commit()
        db.refresh(db_maintenance)

    except IntegrityError:

        db.rollback()
        raise HTTPException(
            409, "Maintenance already exists"
        )
    return db_maintenance

@app.get(
    "/api/maintenances",
    response_model=list[MaintenanceRead], 
)
def get_maintenances(
    db:Session=Depends(get_db),
):
    return db.query(MaintenanceDB).all()

@app.get(
    "/api/prioritys/{priority}",
    response_model=MaintenanceRead,
)
def priority(
    maintenance_id:int,
    db:Session=Depends(get_db),
):
    maintenance=db.get(MaintenanceDB,maintenance_id)
    if priority is None:
        raise HTTPException(
            200, "priority not found"
        )
    return priority
       