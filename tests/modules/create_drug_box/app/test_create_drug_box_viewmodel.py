from src.modules.create_drug_box.app.create_drug_box_viewmodel import CreateDrugBoxViewmodel
from src.shared.infra.repositories.drug_box_repository_mock import DrugBoxRepositoryMock


class Test_CreateDrugBoxViewmodel:
    def test_create_drug_box_viewmodel(self):
        repo = DrugBoxRepositoryMock()
        
        drugbox = repo.drugboxes[0]
        
        drugbox_viewmodel = CreateDrugBoxViewmodel(drugbox).to_dict() 
        
        assert drugbox_viewmodel == {
        'drugbox':{
            'drugbox_id':1,
            'ingestion_type':'GAS',
            'volume':200.0,
            'num_drug':5,
            'total_price':7.5,
            'drug':{
                'name':'Viagrinha',
                'description':'O exercito curte e curto',
                'price':1.5
            }
        },
        'message':'the drugbox was created'
        }