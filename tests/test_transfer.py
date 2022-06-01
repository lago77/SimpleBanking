
import re
import pytest
@pytest.mark.parametrize("amount",[ (24.4), ("24.4"), (-30.404),(0)

 ])
def test_validate_transfer(amount):
    ##this function tests to make sure the balance is not negative or and not a string when entered.

    amount_conditional_isnum= ((isinstance(amount,float) or isinstance(amount,int)))
    
    amount_conditional_greaterthanzero =  (amount>0)

    assert amount_conditional_greaterthanzero == True, "Your transfer amount must be greater than 0"
    assert amount_conditional_isnum == True, "Your transfer amount must be an integer or float"
