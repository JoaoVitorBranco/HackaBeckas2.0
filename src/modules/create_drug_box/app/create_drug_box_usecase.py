from src.shared.domain.entities.drug_box import DrugBox
from src.shared.domain.repositories.drug_box_repository_interface import IDrugBoxRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction


class CreateDrugBoxUsecase:
    def __init__(self, repo_drug_box: IDrugBoxRepository):
        self.repo = repo_drug_box

    def __call__(self, drug_box: DrugBox):
        drug_box_with_same_id = self.repo.get_drugbox(drug_box.drugbox_id)
        if drug_box_with_same_id is not None:
            raise ForbiddenAction("drugbox_id")
        
        return self.repo.create_drugbox(drug_box)