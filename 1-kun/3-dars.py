from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float

products = []

@app.post('/products')
def create_product(product: Product):
    products.append(product)
    return {'message': "Product qo'shildi", 'data': product}

@app.get('/products')
def get_products():
    return{'products': products}

@app.get("/products/{index}")
def get_product(index: int):
    if index < len(products):
        return products[index]
    return {'error': 'topilmadi'}

@app.put('/product/{index}')
def update_pruduct(index: int, product: Product):
    if index < len(products):
        products[index] = product
        return {'message': "Yangilandi", "data": product}
    return {'error': "Topilmadi"}

@app.delete('/products/{index}')
def delete_product(index: int):
    if index < len(products):
        delete = products.pop(index)
        return {'message': "O'chirildi", 'data': delete}
    return {'error': "Topilmadi"}