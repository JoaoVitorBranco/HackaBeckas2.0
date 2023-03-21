import pytest
from src.shared.domain.entities.drug import Drug
from src.shared.helpers.errors.domain_errors import EntityError


class Test_Drug():
    def test_drug(self):
        drug = Drug(name="drug", description="description", price=1.0)
        
        assert drug.name == "drug"
        assert drug.description == "description"
        assert drug.price == 1.0
        
    def test_drug_invalid_name(self):
        with pytest.raises(EntityError):
            drug = Drug(name=1, description="description", price=1.0)
    
    def test_drug_invalid_description(self):
        with pytest.raises(EntityError):
            drug = Drug(name="drug", description=None, price=1.0)
            
    def test_drug_invalid_price(self):
        with pytest.raises(EntityError):
            drug = Drug(name="drug", description="description", price="1.0")