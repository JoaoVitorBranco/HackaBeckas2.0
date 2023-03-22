from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from .create_drug_box_usecase import CreateDrugBoxUsecase
from .create_drug_box_controller import CreateDrugBoxController
from src.shared.infra.repositories.drug_box_repository_mock import DrugBoxRepositoryMock


def create_drug_box_presenter(event, context):
    repo = DrugBoxRepositoryMock()
    usecase = CreateDrugBoxUsecase(repo)
    controller = CreateDrugBoxController(usecase)

    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.to_dict()
