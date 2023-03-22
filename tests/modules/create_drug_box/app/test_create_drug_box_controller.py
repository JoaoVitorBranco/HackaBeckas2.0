from src.modules.create_drug_box.app.create_drug_box_controller import CreateDrugBoxController
from src.modules.create_drug_box.app.create_drug_box_usecase import CreateDrugBoxUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.drug_box_repository_mock import DrugBoxRepositoryMock


class Test_CreateDrugBoxController:
    
    def test_create_drug_box_controller(self):
        repo = DrugBoxRepositoryMock()
        usecase = CreateDrugBoxUsecase(repo)
        controller = CreateDrugBoxController(usecase)
        
        request = HttpRequest(body={
            "drugbox_id": 9,
            "ingestion_type": "GAS",
            "volume": 200.0,
            "num_drug": 5,
            "name": "Viagrinha",
            "description": "O exercito curte e curto",
            "price": 1.5
        }
        )
        
        response = controller(request)
        
        assert response.status_code == 201
        assert response.body["message"] == "the drugbox was created"
        assert response.body["drugbox"]["drugbox_id"] == 9
        assert response.body["drugbox"]["ingestion_type"] == "GAS"
        assert response.body["drugbox"]["volume"] == 200.0
        assert response.body["drugbox"]["num_drug"] == 5
        assert response.body["drugbox"]["total_price"] == 7.5
        assert response.body["drugbox"]["drug"]["name"] == "Viagrinha"
        assert response.body["drugbox"]["drug"]["description"] == "O exercito curte e curto"
        assert response.body["drugbox"]["drug"]["price"] == 1.5
    
    def test_create_drug_box_controller_missing_drugbox_id(self):
        repo = DrugBoxRepositoryMock()
        usecase = CreateDrugBoxUsecase(repo)
        controller = CreateDrugBoxController(usecase)
        
        request = HttpRequest(body={
            "ingestion_type": "GAS",
            "volume": 200.0,
            "num_drug": 5,
            "name": "Viagrinha",
            "description": "O exercito curte e curto",
            "price": 1.5
        }
        )
        
        response = controller(request) 
        
        assert response.status_code == 400
        assert response.body == "Field drugbox_id is missing"
    