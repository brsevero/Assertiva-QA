Feature: Testar a API simples dos personagens de Harry Potter

    Testar os endpoints da api do Harry Potter

Scenario: GET Characters endpoint
    Given I am NOT a logging user
    When I request from API
    Then I receive valid HTTP response code 200
