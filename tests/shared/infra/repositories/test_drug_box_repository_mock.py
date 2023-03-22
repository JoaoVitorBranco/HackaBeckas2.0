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