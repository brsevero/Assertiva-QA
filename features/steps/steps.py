from behave import given, when, then, step, fixture
import requests


@fixture()
def applicaton():
    ajudante = Dados()
    return ajudante

class Dados():
    api_url = 'http://hp-api.herokuapp.com/api'
    response_code = ''

@given('I am NOT a logging user')
def step_impl(applicaton):
    pass

@when('I request from API')
def step_impl(application):
    response = requests.get('http://hp-api.herokuapp.com/api/characters')
    application.response_code = response.status_code

@then('I receive valid HTTP response code 200')
def step_impl(applicaton):
    assert applicaton.response_code == 200
