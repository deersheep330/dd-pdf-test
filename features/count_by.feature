Feature: download pdf with count by families

    Background: on workspace
        Given on ps page
        Then login
        Then navigate to dd page
        Then import patents
        Then start analysis

    Scenario: oi1
        Given on workspace
        Then wait for oi1
        Then change oi1 count by families
        Then change oi1 filter
        Then download oi1 pdf
        Then validate customized oi1 families

    Scenario: oi2
        Given on workspace
        Then wait for oi2
        Then change oi2 count by families
        Then change oi2 filter
        Then download oi2 assignees pdf
        Then validate customized oi2 assignees families
        Then download oi2 inventors pdf
        Then validate customized oi2 inventors families

    Scenario: oi3
        Given on workspace
        Then wait for oi3
        Then change oi3 count by families
        Then change oi3 filter
        Then download oi3 pdf
        Then validate customized oi3 families

    Scenario: hh1
        Given on workspace
        Then wait for hh1
        Then change hh1 count by families
        Then change hh1 filter
        Then download hh1 pdf
        Then validate customized hh1 families
        Then download hh1 transferred pdf
        Then validate customized hh1 transferred families

    Scenario: hh2
        Given on workspace
        Then wait for hh2
        Then change hh2 count by families
        Then change hh2 filter
        Then download hh2 pdf
        Then validate customized hh2 families

    Scenario: qh2
        Given on workspace
        Then wait for qh2
        Then change qh2 count by families
        Then change qh2 filter
        Then download qh2 pdf
        Then validate customized qh2 families