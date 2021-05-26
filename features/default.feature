Feature: download pdf with default settings

    Scenario: download pdf
        Given on ps page
        Then login
        Then navigate to dd page
        Then import patents
        Then start analysis
        Then download pdf