from pydantic import BaseModel, model_validator
from typing import Optional

class User(BaseModel):
    password: str
    confirm_password: str
    
    @model_validator(mode='after')
    def check_password(self):
        # print(vars(self))
        if self.password != self.confirm_password:
            raise ValueError("Password must be the same")
        return self

user = User(password="abc", confirm_password="abc")
# print(user)

class ItemtoShip(BaseModel):
    name: str
    needs_shipping: bool
    shipping_address: Optional[str | int] = ""
    @model_validator(mode="after")
    def check_if_shipping(self):
        if self.needs_shipping and not self.shipping_address:
            raise ValueError("pls, Input shipping address")
        return self

item = ItemtoShip(name="Emma12", needs_shipping=False, shipping_address=234)
print(item)