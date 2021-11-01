from behave import given, when, then, step, fixture
import requests


@fixture()
def applicaton():
    ajudante = Dados()
    return ajudante

class Dados():
    response_code = ''

@given('I am NOT a logging user')
def step_impl(applicaton):
    pass

@when('I request from API with Characters endpoint')
def step_impl(application):
    response = requests.get('http://hp-api.herokuapp.com/api' + '/characters')
    application.response_code = response.status_code

@when('I request from API with Students endpoint')
def step_impl(application):
    response = requests.get('http://hp-api.herokuapp.com/api' + '/characters/students')
    application.response_code = response.status_code

@when('I request from API with Staff endpoint')
def step_impl(application):
    response = requests.get('http://hp-api.herokuapp.com/api' + '/characters/staff')
    application.response_code = response.status_code

@when('I request from API with a house endpoint - Slytherin')
def step_impl(application):
    response = requests.get('http://hp-api.herokuapp.com/api' + '/characters/house/slytherin')
    application.response_code = response.status_code

@when('I request from API with a house endpoint - Gryffindor')
def step_impl(application):
    response = requests.get('http://hp-api.herokuapp.com/api' + '/characters/house/gryffindor')
    application.response_code = response.status_code

@when('I request from API with a house endpoint - Hufflepuff')
def step_impl(application):
    response = requests.get('http://hp-api.herokuapp.com/api' + '/characters/house/hufflepuff')
    application.response_code = response.status_code

@when('I request from API with a house endpoint - Ravenclaw')
def step_impl(application):
    response = requests.get('http://hp-api.herokuapp.com/api' + '/characters/house/Ravenclaw')
    application.response_code = response.status_code

@then('I receive valid HTTP response code 200')
def step_impl(applicaton):
    assert applicaton.response_code == 200
