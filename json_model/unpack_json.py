"""Parsing JSON with Pydantic."""
import json
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
    location: str
    
    @classmethod
    def unpack(cls, file_path: str) -> "Person":
        with open(file_path) as file:
            return cls(**json.loads(file.read()))
    

person = Person.unpack("person.json")
print(person)