import pytest
from src.shared.domain.entities.drug import Drug
from src.shared.domain.entities.drug_box import DrugBox

from src.shared.domain.enums.ingestion_type_enum import INGESTION_TYPE
from src.shared.helpers.errors.domain_errors import EntityError

class Test_DrugBox():
    def test_drug_box(self):
        drug_box = DrugBox(drugbox_id=1, ingestion_type=INGESTION_TYPE.GAS, volume=1.0, num_drug=1, drug=Drug(name="drug", description="description", price=1.0))
        
        assert drug_box.drugbox_id == 1
        assert drug_box.ingestion_type == INGESTION_TYPE.GAS
        assert drug_box.volume == 1.0
        assert drug_box.num_drug == 1
        assert drug_box.drug.name == "drug"
        assert drug_box.drug.description == "description"
        assert drug_box.drug.price == 1.0
        
    def test_drug_box_invalid_drugbox_id(self):
        with pytest.raises(EntityError):
            drug_box = DrugBox(drugbox_id="1", ingestion_type=INGESTION_TYPE.GAS, volume=1.0, num_drug=1, drug=Drug(name="drug", description="description", price=1.0))
    
    def test_drug_box_invalid_ingestion_type(self):
        with pytest.raises(EntityError):
            drug_box = DrugBox(drugbox_id=1, ingestion_type="oral", volume=1.0, num_drug=1, drug=Drug(name="drug", description="description", price=1.0))
    
    def test_drug_box_invalid_volume(self):
        with pytest.raises(EntityError):
            drug_box = DrugBox(drugbox_id=1, ingestion_type=INGESTION_TYPE.GAS, volume="1.0", num_drug=1, drug=Drug(name="drug", description="description", price=1.0))
            
    def test_drug_box_invalid_num_drug(self):
        with pytest.raises(EntityError):
            drug_box = DrugBox(drugbox_id=1, ingestion_type=INGESTION_TYPE.GAS, volume=1.0, num_drug="1", drug=Drug(name="drug", description="description", price=1.0))
            
    def test_drug_box_invalid_drug(self):
        with pytest.raises(EntityError):
            drug_box = DrugBox(drugbox_id=1, ingestion_type=INGESTION_TYPE.GAS, volume=1.0, num_drug=1, drug="drug")
        
         
    