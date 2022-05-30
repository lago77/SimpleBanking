
import re
import pytest
@pytest.mark.parametrize("balance",[ (24.4), ("24.4"), (-30.404),(0)

 ])
def test_validate_balance(balance):
    ##this function tests to make sure the balance is not negative or and not a string when entered.

    balance_conditional_isnum= ((isinstance(balance,float) or isinstance(balance,int)))
    
    balance_conditional_ispositive =  (balance>=0)

    assert balance_conditional_ispositive == True, "Your balance must not be negative"
    assert balance_conditional_isnum == True, "Your balance must be an integer or float"
