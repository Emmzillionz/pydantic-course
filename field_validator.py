from pydantic import BaseModel, field_validator

class User(BaseModel):
    first_name: str
    last_name: str
    age: int
    passed_induction: bool
    years_sevice: int | str | float
    
    @field_validator("first_name", "last_name")
    def check_name(name):
        if not name.isalpha():
            raise ValueError(f"{name} isn't correctly formed!")
        return name.title()
    
    @field_validator("age")
    def check_age(age):
        if age < 18 or age > 100:
            raise ValueError("Bad age!!")
        return age
    
user = User(first_name="emma", last_name="john",age=27, passed_induction=True, years_sevice="2 years")
print(user)