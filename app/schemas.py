from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional, Any


class RoleBase(BaseModel):
    name: str
    description: Optional[str] = None

class RoleCreate(RoleBase):
    pass

class RoleOut(RoleBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class PermissionBase(BaseModel):
    name: str
    description: Optional[str] = None

class PermissionCreate(PermissionBase):
    pass

class PermissionOut(PermissionBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class RolePermissionOut(BaseModel):
    id: int
    role_id: int
    permission_id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    name: Optional[str] = None
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class GuestBase(BaseModel):
    user_id: int

class GuestCreate(GuestBase):
    pass

class GuestOut(GuestBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class RoomBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    capacity: int   # ✅ fix to int
    amenities: Optional[str] = None
    photos: Optional[str] = None

class RoomCreate(RoomBase):
    pass

class RoomOut(RoomBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class RoomAvailabilityBase(BaseModel):
    room_id: int
    date: date
    is_available: bool = True

class RoomAvailabilityOut(RoomAvailabilityBase):
    id: int

    class Config:
        from_attributes = True


class BookingBase(BaseModel):
    user_id: int        
    room_id: int
    check_in: date
    check_out: date
    total_price: Optional[float] = None  
class BookingCreate(BookingBase):
    pass

class BookingOut(BookingBase):
    id: int
    status: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class PaymentBase(BaseModel):
    booking_id: int
    amount: float
    status: str
    transaction_id: Optional[str] = None

class PaymentCreate(PaymentBase):
    pass

class PaymentOut(PaymentBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class TemplateBase(BaseModel):
    name: str
    layout: Optional[Any] = None
    is_active: bool = False

class TemplateCreate(TemplateBase):
    pass

class TemplateOut(TemplateBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class PageBase(BaseModel):
    slug: str
    title: str
    content: Optional[str] = None
    template_id: Optional[int] = None

class PageCreate(PageBase):
    pass

class PageOut(PageBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class PageSectionBase(BaseModel):
    page_id: int
    section_name: Optional[str] = None
    content: Optional[Any] = None
    position: int = 0

class PageSectionCreate(PageSectionBase):
    pass

class PageSectionOut(PageSectionBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    sub: Optional[str] = None
