Feature: download pdf with default settings

    Background: download pdf
        Given on ps page
        Then login
        Then navigate to dd page
        Then import patents
        Then start analysis
        Then download pdf

    Scenario: cs summary
        Given on pdf downloaded
        Then validate cs summary

    Scenario: cs1
        Given on pdf downloaded
        Then validate cs1

    Scenario: cs2
        Given on pdf downloaded
        Then validate cs2

    Scenario: cs3
        Given on pdf downloaded
        Then validate cs3

    Scenario: tech summary
        Given on pdf downloaded
        Then validate tech summary

    Scenario: tech1
        Given on pdf downloaded
        Then validate tech1

    Scenario: tech2
        Given on pdf downloaded
        Then validate tech2

    Scenario: oi summary
        Given on pdf downloaded
        Then validate oi summary

    Scenario: oi1
        Given on pdf downloaded
        Then validate oi1

    Scenario: oi2 assignees
        Given on pdf downloaded
        Then validate oi2 assignees

    Scenario: oi2 inventors
        Given on pdf downloaded
        Then validate oi2 inventors

    Scenario: oi3
        Given on pdf downloaded
        Then validate oi3

    Scenario: hh summary
        Given on pdf downloaded
        Then validate hh summary

    Scenario: hh1
        Given on pdf downloaded
        Then validate hh1

    Scenario: hh1 transferred
        Given on pdf downloaded
        Then validate hh1 transferred

    Scenario: hh2
        Given on pdf downloaded
        Then validate hh2

    Scenario: qv summary
        Given on pdf downloaded
        Then validate qv summary

    Scenario: qv1
        Given on pdf downloaded
        Then validate qv1

    Scenario: qv2
        Given on pdf downloaded
        Then validate qv2

    Scenario: qv3
        Given on pdf downloaded
        Then validate qv3

    Scenario: qh summary
        Given on pdf downloaded
        Then validate qh summary

    Scenario: qh1
        Given on pdf downloaded
        Then validate qh1

    Scenario: qh2
        Given on pdf downloaded
        Then validate qh2

    Scenario: vh summary
        Given on pdf downloaded
        Then validate vh summary

    Scenario: vh1
        Given on pdf downloaded
        Then validate vh1

    Scenario: vh2
        Given on pdf downloaded
        Then validate vh2

    Scenario: vh3 potential targets
        Given on pdf downloaded
        Then validate vh3 potential targets

    Scenario: vh3 family id
        Given on pdf downloaded
        Then validate vh3 family id