from .create_drug_box_usecase import CreateDrugBoxUsecase
from .create_drug_box_viewmodel import CreateDrugBoxViewmodel
from src.shared.domain.entities.drug import Drug
from src.shared.domain.entities.drug_box import DrugBox
from src.shared.domain.enums.ingestion_type_enum import INGESTION_TYPE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Created, InternalServerError, Forbidden
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.helpers.errors.controller_errors import MissingParameters

class CreateDrugBoxController:
    def __init__(self, usecase: CreateDrugBoxUsecase):
        self.createDrugBoxUsecase = usecase
        
    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.data.get("drugbox_id") == None:
                raise MissingParameters("drugbox_id")
            if request.data.get("ingestion_type") == None:
                raise MissingParameters("ingestion_type")
            if request.data.get("volume") == None:
                raise MissingParameters("volume")
            if request.data.get("num_drug") == None:
                raise MissingParameters("num_drug")
            if request.data.get("name") == None:
                raise MissingParameters("name")
            if request.data.get("description") == None:
                raise MissingParameters("description")
            if request.data.get("price") == None:
                raise MissingParameters("price")
            
            if type(request.data.get("ingestion_type")) != str:
                raise EntityError("ingestion_type")
            ingestion_type_values = [val.value for val in INGESTION_TYPE]
            if request.data.get("ingestion_type") not in ingestion_type_values:
                raise EntityError("ingestion_type")
            ingestion_type = INGESTION_TYPE[request.data.get("ingestion_type")]
        
            drug = Drug(name=request.data.get("name"), description=request.data.get("description"), price=float(request.data.get("price")))
            drugbox = DrugBox(drug=drug, drugbox_id=int(request.data.get("drugbox_id")), ingestion_type=ingestion_type, volume=float(request.data.get("volume")), num_drug=int(request.data.get("num_drug")))
            
            drugbox_response = self.createDrugBoxUsecase(drugbox)
            viewmodel = CreateDrugBoxViewmodel(drugbox_response)
            
            return Created(body=viewmodel.to_dict())
            
            
            
    
        except EntityError as err:
            return BadRequest(body=err.message)
            
        except ForbiddenAction as err:
            return Forbidden(body=err.message)
            
        except MissingParameters as err:
            return BadRequest(body=err.message)    
            
        except Exception as err:
            return InternalServerError(body=err.args[0])