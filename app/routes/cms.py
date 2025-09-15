from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/cms", tags=["CMS"])


# -------- Templates --------
@router.post("/templates", response_model=schemas.TemplateOut)
def create_template(template: schemas.TemplateCreate, db: Session = Depends(get_db)):
    new_template = models.Template(**template.dict())
    db.add(new_template)
    db.commit()
    db.refresh(new_template)
    return new_template


@router.get("/templates", response_model=list[schemas.TemplateOut])
def list_templates(db: Session = Depends(get_db)):
    return db.query(models.Template).all()


# -------- Pages --------
@router.post("/pages", response_model=schemas.PageOut)
def create_page(page: schemas.PageCreate, db: Session = Depends(get_db)):
    new_page = models.Page(**page.dict())
    db.add(new_page)
    db.commit()
    db.refresh(new_page)
    return new_page


@router.get("/pages", response_model=list[schemas.PageOut])
def list_pages(db: Session = Depends(get_db)):
    return db.query(models.Page).all()


# -------- Page Sections --------
@router.post("/sections", response_model=schemas.PageSectionOut)
def create_section(section: schemas.PageSectionCreate, db: Session = Depends(get_db)):
    new_section = models.PageSection(**section.dict())
    db.add(new_section)
    db.commit()
    db.refresh(new_section)
    return new_section


@router.get("/sections", response_model=list[schemas.PageSectionOut])
def list_sections(db: Session = Depends(get_db)):
    return db.query(models.PageSection).all()
