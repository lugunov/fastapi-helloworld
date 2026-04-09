from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
from schemas import FiatPurchaseCreate, FiatPurchaseResponse
from crud import create_fiat_purchase, get_fiat_purchases

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hello FastAPI")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}

@app.post("/purchases", response_model=FiatPurchaseResponse)
def create_purchase(purchase: FiatPurchaseCreate, db: Session = Depends(get_db)):
    return create_fiat_purchase(db, purchase)

@app.get("/purchases", response_model=list[FiatPurchaseResponse])
def list_purchases(db: Session = Depends(get_db)):
    return get_fiat_purchases(db)