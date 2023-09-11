from typing import Union
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name" : "Foo"},
                 {"item_name" : "Bar"},
                 {"item_name : Baz"}
                 ]

#http://localhost:8000/items/?skip={value}&limit={value}
#default value is skip:0 limit:10 so,
#http://localhost:8000/items/?skip=20 or ?limit=10 also allow
@app.get("/items/")
async def read_item(skip : int = 0, limit : int = 10):
    return fake_items_db[skip : skip + limit]

#선택적 매개변수
#q에 해당 되는 부분에 값을 안넣어도 둘다 넣지 않아도 요청은 성공한다
@app.get("/items/{item_id}")
async def read_item(item_id:str,q:Union[str,None]=None):
    if q:
        return {"item_id":item_id, "q":q}
    return {"item_id":item_id}

