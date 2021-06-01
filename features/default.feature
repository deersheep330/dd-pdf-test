Feature: download pdf with default settings

    Scenario: download pdf
        Given on ps page
        Then login
        Then navigate to dd page
        Then import patents
        Then start analysis
        Then download pdf
        Then validate cs summary
        Then validate cs1
        Then validate cs2
        Then validate cs3
        Then validate tech summary
        Then validate tech1
        Then validate tech2
        Then validate oi summary
        Then validate oi1
        Then validate oi2 assignees
        Then validate oi2 inventors
        Then validate oi3
        Then validate hh summary
        Then validate hh1
        Then validate hh1 transferred
        Then validate hh2
        Then validate qv summary
        Then validate qv1
        Then validate qv2
        Then validate qv3
        Then validate qh summary
        Then validate qh1
        Then validate qh2
        Then validate vh summary
        Then validate vh1
        Then validate vh2
        Then validate vh3 potential targets
        Then validate vh3 family id