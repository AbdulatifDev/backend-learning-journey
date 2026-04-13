from database import engine
from models import Base

Base.metadata.create_all(bind=engine)


from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models

app = FastAPI()

# DB ulanish
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE
@app.post("/products")
def create_product(name: str, price: int, db: Session = Depends(get_db)):
    new_product = models.Product(name=name, price=price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

# READ
@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

@app.get("/products/{id}")
def get_product(id: int, db: Session = Depends(get_db)):
   product = db.query(models.Product).get(id)
   return product.name

@app.get("/product/count")
def count_column(db: Session = Depends(get_db)):
    return db.query(models.Product).count()


@app.delete("/products/{id}")
def delete_products(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).get(id)
    db.delete(product)
    db.commit()
    return {"message": f" {product.name} Maxsulot o'chirildi!"}

@app.put("/products/{id}")
def update_product(id: int, price = float, db: Session = Depends(get_db)):
    product = db.query(models.Product).get(id)
    product.price = price
    db.commit()
    return{"message": f"{product.name} Maxsulot o'zgartirildi"}
    
