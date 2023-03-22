from abc import ABC, abstractmethod

from src.shared.domain.entities.drug_box import DrugBox


class IDrugBoxRepository(ABC):
    @abstractmethod
    def create_drugbox(self, drugbox: DrugBox) -> DrugBox:
        pass
    
    
   
   