from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@given('que entrei no site do "maganize luiza"')
def step_impl(context):
    context.driver.get("https://www.magazineluiza.com.br/")

@when('digitar "relogio" na barra de busca')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-search').send_keys("relogio")   

@when('clicar em "lupa"')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, 'sc-dkPtRN.gQoOew').click()
    sleep(5)

@when('clicar no primeiro item')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, 'sc-jgrJph.csTYkH').click()

@when('clicar em aceitar Cookies')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, 'text-button-cookie').click()

@when('clicar em "adicionar na sacola"')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, 'button__text').click()

@then('o produto foi adicionado na sacola')
def step_impl(context):
    pass 

