from src.shared.domain.entities.drug_box import DrugBox
from src.shared.domain.enums.ingestion_type_enum import INGESTION_TYPE
from src.shared.infra.repositories.drug_box_repository_mock import DrugBoxRepositoryMock


class Test_DrugBoxRepositoryMock:
    def test_create_drugbox(self):
        repo = DrugBoxRepositoryMock()
        length_before = len(repo.drugboxes)
        
        drugbox = DrugBox(drugbox_id=5, ingestion_type=INGESTION_TYPE.GAS, volume=200.5, num_drug=9, drug=repo.drugs[1])
        
        drugbox_response = repo.create_drugbox(drugbox=drugbox)
        
        length_after = len(repo.drugboxes)
        
        assert length_after == length_before + 1
        assert drugbox_response == drugbox 
        
    def test_get_drugbox(self):
        repo = DrugBoxRepositoryMock()
        
        drugbox = repo.get_drugbox(drugbox_id=repo.drugboxes[0].drugbox_id) 
        
        assert drugbox == repo.drugboxes[0]
        
    def test_get_drugbox_not_found(self):
        repo = DrugBoxRepositoryMock()
        
        drugbox = repo.get_drugbox(drugbox_id=-1) 
        
        assert drugbox == None
    