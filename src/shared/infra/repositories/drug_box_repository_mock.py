from src.shared.domain.entities.drug import Drug
from src.shared.domain.entities.drug_box import DrugBox
from src.shared.domain.enums.ingestion_type_enum import INGESTION_TYPE
from src.shared.domain.repositories.drug_box_repository_interface import IDrugBoxRepository


class DrugBoxRepositoryMock(IDrugBoxRepository):
    drugboxes: list[DrugBox]
    drugs: list[Drug]
    
    def __init__(self):
        self.drugs = [
            Drug(name="Besetacil", description="Nao sei qq eh isso", price=50.0),
            Drug(name="Novalgina", description="Uma pilula magica marrom", price=150.0),
            Drug(name="Viagrinha", description="O exercito curte e curto", price=1.5)
        ]
        
        self.drugboxes = [
            DrugBox(drugbox_id=1, ingestion_type=INGESTION_TYPE.GAS, volume=200.0, num_drug=5, drug=self.drugs[2]),
            DrugBox(drugbox_id=2, ingestion_type=INGESTION_TYPE.LIQUID, volume=50.0, num_drug=1, drug=self.drugs[2]),
            DrugBox(drugbox_id=3, ingestion_type=INGESTION_TYPE.COMPRIMID, volume=25.0, num_drug=10, drug=self.drugs[1]),
            DrugBox(drugbox_id=4, ingestion_type=INGESTION_TYPE.GAS, volume=2.5, num_drug=100, drug=self.drugs[0])
        ]
        
    def create_drugbox(self, drugbox: DrugBox) -> DrugBox:
        self.drugboxes.append(drugbox)
        return drugbox
    
    def get_drugbox(self, drugbox_id: int) -> DrugBox:
        for drugbox in self.drugboxes:
            if drugbox.drugbox_id == drugbox_id:
                return drugbox
        return None
        
        
        
        