import uvicorn
import names

from fastapi import FastAPI

import schemas 

api = FastAPI()

cats = []

@api.get("/")
def test():
    return cats

@api.put("/add")
def add_cat(cat: schemas.Cat):
    cats.append(cat)
    

if __name__ == '__main__':
    uvicorn.run('main:api', reload=True)

