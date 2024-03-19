from dataclasses import dataclass

@dataclass
class Dog():
    name: str
    age: int
    
d = Dog('Sharik','3')

print(d.name)


from pydantic import BaseModel
from typing import Iterable, Tuple


class Cat(BaseModel):
    name: str
    age: int
    colors: Iterable[str]
    dimensions: Tuple[int,int]
    
c = Cat(name="Murzik", age=8, colors=['grey','ginger'], dimensions=[2,3])
print(type(d.age), type(c.age))