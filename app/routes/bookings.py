from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db


router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.post("/", response_model=schemas.BookingOut)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    # basic availability check (example)
    # compute and save
    db_booking = models.Booking(
    user_id=booking.user_id,
    room_id=booking.room_id,
    check_in=booking.check_in,
    check_out=booking.check_out,
    total_price=booking.total_price,
    status="pending"
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    print("Saved booking:", db_booking)
    return db_booking


@router.get("/", response_model=list[schemas.BookingOut])
def list_bookings(db: Session = Depends(get_db)):
    return db.query(models.Booking).all()


@router.get("/{booking_id}", response_model=schemas.BookingOut)
def get_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(models.Booking).get(booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking