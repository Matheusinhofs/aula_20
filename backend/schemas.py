from pydantic import BaseModel, PositiveFloat, EmailStr, validator, Field
from enum import Enum
from datetime import datetime
from typing import Optional

# o schema é muito semelhante ao model mas vai trazer os campos do banco sem id e created_at
# schema vai ser como uma view e com validação
# model vai comunicar com o banco e deve ser igual a ela
# o schema vai ser a view, sendo uma representação dos dados que o usuário vai inserir, mas não necessariamente os dois são iguais

class ProductBase(BaseModel):
    name: str
    description: str
    price: PositiveFloat
    categoria: str
    email_fornecedor: EmailStr

class ProductCreate(ProductBase):
    pass

# Esse class response é como se fosse o select do banco
class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# O optional permite que o usuário altere, de forma opcional um campo ou mais
class ProductUpdate(BaseModel):
   name: Optional[str] = None
   description: Optional[str] = None
   price: Optional[PositiveFloat] = None
   categoria: Optional[str] = None
   email_fornecedor: Optional[EmailStr] = None


