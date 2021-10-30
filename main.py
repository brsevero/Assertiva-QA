import pytest
import requests
from pytest_bdd import scenario, given, when, then

@pytest.fixture

def application():
    helper = Dados()
    return helper

class Dados():
    livros_total = None
    log = ""
    logStatus = None

@scenario('LOR.feature', 'Get the list of book')
def test_GetTheListOfBook():
    pass

@given("I am NOT a logging user")
def LoggingUser():
    pass

@when("I request the application")
def RequestTheApplication():
    response = requests.get("https://the-one-api.dev/v2/book")
    data = response.json()
    application().livros_total = data["total"]
    print(application().livros_total)
    assert data["status"] == 200

@then("I get a JSON with information about the total of books")
def CheckingTotalofBooks():
    assert application().livros_total == 3