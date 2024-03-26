import requests
from json import *
from datetime import datetime 

from schemas import Cat
import names
import random

s= requests.Session()
s.trust_env = False

api_base='http://127.0.0.1:8000'

for _ in range(5):
    random.seed(2.718281828459045235360287471352*datetime.now().timestamp())
    c= Cat(name=names.get_first_name(), age=random.randrange(0,20), 
        colors=['grey','ginger'], dimensions=[random.randrange(2,6),random.randrange(2,6)])
    s.put(f"{api_base}/add", c.model_dump_json())
    

r = s.get(api_base)
for c_json in r.json():
    c= Cat.model_validate(r.json()[0])
    print(c, c.colors)