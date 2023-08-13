from enum import Enum
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

#누군가가 URI로 "/" 요청시 조회할수 있는 것들
@app.get("/")
def read_root():
    return{"hello":"world"}

@app.get("/hello")
def hello():
    return "hello world"

#get method
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

#만약에 URL이 같은데 URI에서 혼동이 있을수 있는 경우,
#아래와 같이 먼저 선언해주어야합니다.
#경로 동작은 순차적으로 작동하기 때문에 "para/{info}"가 작동하기 전에 "para/learn"
#이 먼저 작동하도록 먼저 작성해주는 겁니다.
@app.get("para/learn")
async def para_send():
    return {"info": "it's should be first"}
#route parameter값으로 값 전달 방법
#아래와 같이 데코레이션에 문자열 포맷으로 변수를 넣어주면 요청시
#해당 정보로 변수에 넣을수 있다.
#또한 함수의 파라미터 값에 데이터 타입을 지정하면 해당 데이터 타입으로만
#값을 넣을수 있다.
@app.get("para/{info}")
async def para_send(info:int):
    return {"info": info}

#사전정의 값
#enum를 사용하면사전정의 값을 사용할수 있습니다.
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    #1번 방법
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
    #2번방법
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    #3번방법
    return {"model_name": model_name, "message": "Have some residuals"}

@app.put("/items/{item_id}")
def update_item(item_id:int,item:Item):
    return {"item_name":item.name,"item_id":item_id}

#파일넘겨주는 방법
#그냥 home/inseong/myfile.txt를 file_path에 넣어주면 댬
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}