from src.shared.domain.entities.drug_box import DrugBox
from src.shared.domain.repositories.drug_box_repository_interface import IDrugBoxRepository


class CreateDrugBoxUsecase:
    def __init__(self, repo_drug_box: IDrugBoxRepository):
        self.repo = repo_drug_box

    def __call__(self, drug_box: DrugBox):
        