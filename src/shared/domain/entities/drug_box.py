import abc
from src.shared.domain.entities.drug import Drug
from src.shared.domain.enums.ingestion_type_enum import INGESTION_TYPE
from src.shared.helpers.errors.domain_errors import EntityError


class DrugBox(abc.ABC):
    drugbox_id: int
    ingestion_type: INGESTION_TYPE
    volume: float
    num_drug: int
    drug: Drug
    
    def __init__(self, drugbox_id: int, ingestion_type: INGESTION_TYPE, volume: float, num_drug: int, drug: Drug):
        if type(drugbox_id) != int:
            raise EntityError("drugbox_id")
        self.drugbox_id = drugbox_id
        
        if type(ingestion_type) != INGESTION_TYPE:
            raise EntityError("ingestion_type")
        self.ingestion_type = ingestion_type
        
        if type(volume) != float:
            raise(EntityError("volume"))
        self.volume = volume
        
        if type(num_drug) != int:
            raise EntityError("num_drug")
        self.num_drug = num_drug
        
        if type(drug) != Drug:
            raise EntityError("drug")
        self.drug = drug 
    