from sqlalchemy.orm import Session
from typing import List, Optional
from app import models, schemas
from app.auth import get_password_hash

# -------------------
# User
# -------------------
def get_user(db: Session, user_id: int) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        name=user.name,
        email=user.email,
        password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def list_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
    return db.query(models.User).offset(skip).limit(limit).all()


# -------------------
# Roles & Permissions
# -------------------
def create_role(db: Session, role: schemas.RoleCreate) -> models.Role:
    db_role = models.Role(**role.dict())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def list_roles(db: Session) -> List[models.Role]:
    return db.query(models.Role).all()

def create_permission(db: Session, permission: schemas.PermissionCreate) -> models.Permission:
    db_permission = models.Permission(**permission.dict())
    db.add(db_permission)
    db.commit()
    db.refresh(db_permission)
    return db_permission

def list_permissions(db: Session) -> List[models.Permission]:
    return db.query(models.Permission).all()

def assign_permission_to_role(db: Session, role_id: int, permission_id: int) -> models.RolePermission:
    rp = models.RolePermission(role_id=role_id, permission_id=permission_id)
    db.add(rp)
    db.commit()
    db.refresh(rp)
    return rp


# -------------------
# Guests
# -------------------
def create_guest(db: Session, guest: schemas.GuestCreate) -> models.Guest:
    db_guest = models.Guest(**guest.dict())
    db.add(db_guest)
    db.commit()
    db.refresh(db_guest)
    return db_guest

def list_guests(db: Session) -> List[models.Guest]:
    return db.query(models.Guest).all()


# -------------------
# Rooms & Availability
# -------------------
def create_room(db: Session, room: schemas.RoomCreate) -> models.Room:
    db_room = models.Room(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

def list_rooms(db: Session) -> List[models.Room]:
    return db.query(models.Room).all()

def set_room_availability(db: Session, availability: schemas.RoomAvailabilityBase) -> models.RoomAvailability:
    db_avail = models.RoomAvailability(**availability.dict())
    db.add(db_avail)
    db.commit()
    db.refresh(db_avail)
    return db_avail

def list_availability(db: Session, room_id: int) -> List[models.RoomAvailability]:
    return db.query(models.RoomAvailability).filter(models.RoomAvailability.room_id == room_id).all()


# -------------------
# Bookings
# -------------------
def create_booking(db: Session, booking: schemas.BookingCreate) -> models.Booking:
    db_booking = models.Booking(**booking.dict(), status="pending")
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

def list_bookings(db: Session) -> List[models.Booking]:
    return db.query(models.Booking).all()

def get_booking(db: Session, booking_id: int) -> Optional[models.Booking]:
    return db.query(models.Booking).filter(models.Booking.id == booking_id).first()

def update_booking_status(db: Session, booking_id: int, status: str) -> Optional[models.Booking]:
    booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if booking:
        booking.status = status
        db.commit()
        db.refresh(booking)
    return booking


# -------------------
# Payments
# -------------------
def create_payment(db: Session, payment: schemas.PaymentCreate) -> models.Payment:
    db_payment = models.Payment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def list_payments(db: Session) -> List[models.Payment]:
    return db.query(models.Payment).all()


# -------------------
# Templates & CMS
# -------------------
def create_template(db: Session, template: schemas.TemplateCreate) -> models.Template:
    db_template = models.Template(**template.dict())
    db.add(db_template)
    db.commit()
    db.refresh(db_template)
    return db_template

def list_templates(db: Session) -> List[models.Template]:
    return db.query(models.Template).all()

def create_page(db: Session, page: schemas.PageCreate) -> models.Page:
    db_page = models.Page(**page.dict())
    db.add(db_page)
    db.commit()
    db.refresh(db_page)
    return db_page

def list_pages(db: Session) -> List[models.Page]:
    return db.query(models.Page).all()

def create_page_section(db: Session, section: schemas.PageSectionCreate) -> models.PageSection:
    db_section = models.PageSection(**section.dict())
    db.add(db_section)
    db.commit()
    db.refresh(db_section)
    return db_section

def list_page_sections(db: Session, page_id: int) -> List[models.PageSection]:
    return db.query(models.PageSection).filter(models.PageSection.page_id == page_id).all()
