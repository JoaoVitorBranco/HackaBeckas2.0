from src.shared.domain.entities.drug import Drug
from src.shared.domain.entities.drug_box import DrugBox
from src.shared.domain.enums.ingestion_type_enum import INGESTION_TYPE

class DrugViewmodel:
    name: str
    description: str
    price: float
    
    def __init__(self, drug: Drug):
        self.name = drug.name
        self.description = drug.description
        self.price = drug.price
        
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price
        }

class DrugBoxViewmodel:
    drugbox_id: int
    ingestion_type: INGESTION_TYPE
    volume: float
    num_drug: int
    price: float
    drug: DrugViewmodel
    
    def __init__(self, drugbox: DrugBox):
        self.drugbox_id = drugbox.drugbox_id
        self.ingestion_type = drugbox.ingestion_type
        self.volume = drugbox.volume
        self.num_drug = drugbox.num_drug
        self.price = drugbox.num_drug * drugbox.drug.price
        self.drug = DrugViewmodel(drugbox.drug)

    def to_dict(self):
        return {
            "drugbox_id": self.drugbox_id,
            "ingestion_type": self.ingestion_type.value,
            "volume": self.volume,
            "num_drug": self.num_drug,
            "price": self.price,
            "drug": self.drug.to_dict()
        }

class CreateDrugBoxViewmodel:
    drugbox: DrugBoxViewmodel
    
    def __init__(self, drugbox: DrugBox):
        self.drugbox = DrugBoxViewmodel(drugbox)
    
    def to_dict(self):
        return {
            'drugbox': self.drugbox.to_dict(),
            'message': "the drugbox was created"
        }