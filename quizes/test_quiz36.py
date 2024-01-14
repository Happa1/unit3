#test_quiz36.py
import pytest
from quiz_036 import Account


def test_empty_account():
    new_account = Account()
    assert  new_account.balance == 0
    assert  new_account.holder_name == ""
    assert  new_account.holder_email == ""
    number = new_account.number
    assert  isinstance(number, list)
    acc_no = new_account.get_account_no().split('-')
    assert len(acc_no)==3 and len(acc_no[0])==3 and len(acc_no[1])==5 and len(acc_no[2])==1

def test_create_account():
    new_a = Account()
    assert  new_a.get_balance() == 0
    assert  new_a.set_holer_name(name="bob") == "Holder's name is Bob"
    assert new_a.set_holder_email(email="bob@xy.z") == "Holder's email is bob@xy.z"
    assert  new_a.deposit(amount=100)== "New balance: 100 USD"