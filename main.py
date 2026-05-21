from fastapi import FastAPI
from models import Product
app = FastAPI()

@app.get("/")
def greet():
    return "Hello, Girish Here!"

products = [
    Product(id=1, name="phone", description="budget phone", price=99, quantity=10),
    Product(id=2, name="laptop", description="gmaing laptop", price=999, quantity=6)
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id:int):
    for product in products:
        if product.id == id:
            return products[id-1]
        
        return "Product not found"
    

@app.post("/product")
def add_product(product:Product):
    products.append(product)
    return product
            
@app.put("/product")
def update_product(id:int, product:Product):
    for i in range(len(products)):
       if products[i].id == id:
           products[i] = product
           return "Prouct added Sucessfully"
       
    return "Product not found"

@app.delete("/product")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i];
            return "product deleted sucessfully"
    return "Product not found"