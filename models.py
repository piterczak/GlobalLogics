from typing import Optional
from pydantic import BaseModel
from uuid import UUID, uuid4


#Creating class with products that will be described
class Product(BaseModel):
    #id: Optional[UUID] = uuid4       #with id that changes everytime we restart application,
    name: str                        #name which is a string type
    warehouse_count: int             #count of items in shop warehouse
    buy_ammount: Optional[int]                 #ammount of products that user wants to buy

