Feature: Testar a API simples dos personagens de Harry Potter

    Testar os endpoints da api do Harry Potter

Scenario: GET Characters endpoint
    Given I am NOT a logging user
    When I request from API with Characters endpoint
    Then I receive valid HTTP response code 200

Scenario: GET Students endpoint
    Given I am NOT a logging user
    When I request from API with Students endpoint
    Then I receive valid HTTP response code 200

Scenario: GET Staff endpoint
    Given I am NOT a logging user
    When I request from API with Staff endpoint
    Then I receive valid HTTP response code 200

Scenario: GET Slytherin endpoint
    Given I am NOT a logging user
    When I request from API with a house endpoint - Slytherin
    Then I receive valid HTTP response code 200

Scenario: GET Gryffindor endpoint
    Given I am NOT a logging user
    When I request from API with a house endpoint - Gryffindor
    Then I receive valid HTTP response code 200

Scenario: GET Hufflepuff endpoint
    Given I am NOT a logging user
    When I request from API with a house endpoint - Hufflepuff
    Then I receive valid HTTP response code 200

Scenario: GET Ravenclaw endpoint
    Given I am NOT a logging user
    When I request from API with a house endpoint - Ravenclaw
    Then I receive valid HTTP response code 200