Feature: download pdf with adjusted filter settings

    Background: on workspace
        Given on ps page
        Then login
        Then navigate to dd page
        Then import patents
        Then start analysis

    Scenario: cs1
        Given on workspace
        Then wait for cs1
        Then change cs1 filter
        Then download cs1 pdf
        Then validate customized cs1

    Scenario: cs2
        Given on workspace
        Then wait for cs2
        Then change cs2 filter
        Then download cs2 pdf
        Then validate customized cs2

    Scenario: cs3
        Given on workspace
        Then wait for cs3
        Then change cs3 filter
        Then download cs3 pdf
        Then validate customized cs3