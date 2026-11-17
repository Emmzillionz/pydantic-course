from pydantic import BaseModel, Field, field_validator

class User(BaseModel):
    # gt- Greater than | ge- Greater than or Equal to | lt- less than | le- Less than or equal to
    name: str = Field(min_length=1,max_length=100)
    age: int = Field(gt=0, le=120)
    email: str = Field(description="This must be company email")
    website: str = Field(pattern=r"^https?://.*")
    model: str = Field(default="gpt-6")
    items: list[str] = Field(min_length=1)
    
class Users(BaseModel):
    username: str
    
    # Field validator is a decorator from pydantic
    @field_validator("username")
    def validate_username(cls, v):
        if " " in v:
            raise ValueError("Username cannot contain spaces")
        return v

user = User(name="Emma", age=30, email="emmy@gmail.com",website="https://www.clay.com",items=["container"])
username = Users(username="Alice")
print(username.username)
