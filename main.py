from fastapi import FastAPI
from src.modules.create_drug_box.app.create_drug_box_presenter import create_drug_box_presenter


app = FastAPI()


@app.post("/create_drug_box/")
def create_drug_box(data: dict = None):
    event = {
        "body":{
            k:str(v) for k,v in data.items()
        }
    }
    
    response = create_drug_box_presenter(event, None)
    return response