
import pytest
from src.modules.create_drug_box.app.create_drug_box_usecase import CreateDrugBoxUsecase
from src.shared.domain.entities.drug_box import DrugBox
from src.shared.domain.enums.ingestion_type_enum import INGESTION_TYPE
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.infra.repositories.drug_box_repository_mock import DrugBoxRepositoryMock


class Test_CreateDrugBoxUsecase:
    def test_create_drugbox_usecase(self):
        repo = DrugBoxRepositoryMock()
        usecase = CreateDrugBoxUsecase(repo)
        
        drugbox = DrugBox(drugbox_id=5, ingestion_type=INGESTION_TYPE.GAS, volume=200.5, num_drug=9, drug=repo.drugs[1])
        
        length_before = len(repo.drugboxes)
        
        drugbox_response = usecase(drug_box=drugbox)
        
        length_after = len(repo.drugboxes)
        
        assert length_after == length_before + 1
        assert drugbox_response == drugbox
        
    def test_create_drugbox_usecase_drugbox_id_already_exists(self):
        repo = DrugBoxRepositoryMock()
        usecase = CreateDrugBoxUsecase(repo)
        
        drugbox = DrugBox(drugbox_id=1, ingestion_type=INGESTION_TYPE.GAS, volume=200.5, num_drug=9, drug=repo.drugs[1])
        
        with pytest.raises(ForbiddenAction):
            drugbox_response = usecase(drug_box=drugbox)
        
        
        