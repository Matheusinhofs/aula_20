from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ProductResponse, ProductUpdate, ProductCreate
from typing import List
from crud import (
    create_product,
    get_products,
    get_product,
    delete_product,
    update_product,
)

router = APIRouter()

# criar rota de buscar todos os itens
# sempre vão ter dois atributos obrigatórios, o PATH e o RESPONSE
@router.get("/product/", response_model=list[ProductResponse])
def read_all_products(db: Session = Depends(get_db)):
    products = get_products
    return products

# criar rota de buscar 1 item
@router.get("/product/{product_id}", response_model=list[ProductResponse])
def read_one_product(product_id: int, db:Session = Depends(get_db)):
    db_product = get_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Você esta buscando um produto que não existe")

# criar rota de adicionar 1 item
@router.post("/products/", response_model=ProductResponse)
def create_product(product: ProductCreate, db:Session = Depends(get_db)):
    return create_product(product=product, db=db)

# criar uma rota para deletar 1 item
@router.delete("/products/{product_id}", response_model=ProductResponse)
def delete_product(product_id: int, db:Session = Depends(get_db)):
    product_db = delete_product(product_id=product_id, db=db)
    if product_db is None:
        raise HTTPException(status_code=404, detail="Você esta deletando um produto que não existe")
    return delete_product(product_id=product_id, db=db)

# criar uma rota para dar update em 1 item
@router.put("/products/{product_id}", response_model=ProductResponse)
def atualizar_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    product_db = update_product(db=db, product_id=product_id, product=product)
    if product_db is None:
        raise HTTPException(status_code=404, detail="Você esta deletando um produto que não existe")
    return update_product(db=db, product_id=product_id, product=product)
