from pydantic import BaseModel, EmailStr
from dataclasses import dataclass

class User(BaseModel):
    name: str   # Required
    email: EmailStr   # Required
    age: int    # Required
    location: str | None = None  # Optional (has default)
    model: str = "gpt-6-luna" # Default value

def greetuser(user: User):
    return f"Hello, {user.name}! Happy birthday on your {user.age}th birthday"

def load_user(data: dict):
    return user.model_validate(data)

user = User(name="Emma", age="45", email="dave@gmail.com",)

# to convert to dict
user_dict = user.model_dump()

# to convert to JSON string
user_json = user.model_dump_json(indent=2)
print(user_dict)
# print(user_json)

userz = load_user(user_dict) 
message = greetuser(userz)

# Access the dict data like this
print(message)
