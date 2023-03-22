import json
from src.modules.create_drug_box.app.create_drug_box_presenter import create_drug_box_presenter


class Test_CreateDrugBoxPresenter:
    def test_create_drug_box_presenter(self):
        event = {
            "body":{
                "drugbox_id": 9,
                "ingestion_type": "GAS",
                "volume": 200.0,
                "num_drug": 5,
                "name": "Viagrinha",
                "description": "O exercito curte e curto",
                "price": 1.5
            }
        }
        
        response = create_drug_box_presenter(event, None)
        
        expected = {"drugbox": {"drugbox_id": 9, "ingestion_type": "GAS", "volume": 200.0, "num_drug": 5, "total_price": 7.5, "drug": {"name": "Viagrinha", "description": "O exercito curte e curto", "price": 1.5}}, "message": "the drugbox was created"}
        
        assert response["status_code"] == 201
        assert json.loads(response["body"]) == expected