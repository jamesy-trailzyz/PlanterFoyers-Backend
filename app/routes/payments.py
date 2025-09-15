from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/payments", tags=["Payments"])


@router.post("/", response_model=schemas.PaymentOut)
def create_payment(payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    booking = db.query(models.Booking).get(payment.booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    new_payment = models.Payment(**payment.dict())
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment


@router.get("/", response_model=list[schemas.PaymentOut])
def list_payments(db: Session = Depends(get_db)):
    return db.query(models.Payment).all()


@router.get("/{payment_id}", response_model=schemas.PaymentOut)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(models.Payment).get(payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment
