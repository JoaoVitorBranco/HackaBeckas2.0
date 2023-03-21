import abc
from src.shared.helpers.errors.domain_errors import EntityError



class Drug(abc.ABC):
    name: str
    description: str
    price: float
    
    def __init__(self, name: str, description: str, price: float):
        if type(name) != str:
            raise EntityError("name")
        self.name = name
        
        if type(description) != str:
            raise EntityError("description")
        self.description = description
        
        if not self.validate_price(price=price):
            raise EntityError("price")
        self.price = price
    
    @staticmethod
    def validate_price(price: float) -> bool:
        if type(price) != float:
            return False
        if price < 0:
            return False
        return True