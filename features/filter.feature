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

    Scenario: tech1
        Given on workspace
        Then wait for tech1
        Then change tech1 filter
        Then download tech1 pdf
        Then validate customized tech1

    Scenario: tech2
        Given on workspace
        Then wait for tech2
        Then change tech2 filter
        Then download tech2 pdf
        Then validate customized tech2

    Scenario: oi1
        Given on workspace
        Then wait for oi1
        Then change oi1 filter
        Then download oi1 pdf
        Then validate customized oi1

    Scenario: oi2
        Given on workspace
        Then wait for oi2
        Then change oi2 filter
        Then download oi2 assignees pdf
        Then validate customized oi2 assignees
        Then download oi2 inventors pdf
        Then validate customized oi2 inventors

    Scenario: oi3
        Given on workspace
        Then wait for oi3
        Then change oi3 filter
        Then download oi3 pdf
        Then validate customized oi3

    Scenario: hh1
        Given on workspace
        Then wait for hh1
        Then change hh1 filter
        Then download hh1 pdf
        Then validate customized hh1
        Then download hh1 transferred pdf
        Then validate customized hh1 transferred

    Scenario: hh2
        Given on workspace
        Then wait for hh2
        Then change hh2 filter
        Then download hh2 pdf
        Then validate customized hh2

    Scenario: qv1
        Given on workspace
        Then wait for qv1
        Then change qv1 filter
        Then download qv1 pdf
        Then validate customized qv1

    Scenario: qv2
        Given on workspace
        Then wait for qv2
        Then change qv2 filter
        Then download qv2 pdf
        Then validate customized qv2

    Scenario: qv3
        Given on workspace
        Then wait for qv3
        Then change qv3 filter
        Then download qv3 pdf
        Then validate customized qv3

    Scenario: qh1
        Given on workspace
        Then wait for qh1
        Then change qh1 filter
        Then download qh1 pdf
        Then validate customized qh1

    Scenario: qh2
        Given on workspace
        Then wait for qh2
        Then change qh2 filter
        Then download qh2 pdf
        Then validate customized qh2

    Scenario: vh1
        Given on workspace
        Then wait for vh1
        Then change vh1 filter
        Then download vh1 quantity pdf
        Then validate customized vh1
        Then download vh1 percentage pdf
        Then validate customized vh1

    Scenario: vh2
        Given on workspace
        Then wait for vh2
        Then change vh2 filter
        Then download vh2 pdf
        Then validate customized vh2

    Scenario: vh3
        Given on workspace
        Then wait for vh3
        Then change vh3 filter
        Then download vh3 potential targets pdf
        Then validate customized vh3 potential targets
        Then vh3 switch to family id tab
        Then download vh3 family id pdf
        Then validate customized vh3 family id
