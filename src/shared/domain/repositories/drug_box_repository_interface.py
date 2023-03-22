from abc import ABC, abstractmethod

from src.shared.domain.entities.drug_box import DrugBox


class IDrugBoxRepository(ABC):
    @abstractmethod
    def create_drugbox(self, drugbox: DrugBox) -> DrugBox:
        pass
    
    @abstractmethod
    def get_drugbox(self, drugbox_id: int) -> DrugBox:
        pass
    
    
    
   
   