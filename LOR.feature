Feature: The Lord of the Rings API

    All the tests of LOR API

    Scenario: Get the list of book
        Given I am NOT a logging user
        When I request the application
        Then I get a JSON with information about the total of books

    Scenario: Get information about a specific book
        Given I am NOT a logging user
        And I have the ID of the book
        When I request the application
        Then I get a JSON with information about the book
