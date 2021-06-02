Feature: download pdf with adjusted select data

    Background: on workspace
        Given on ps page
        Then login
        Then navigate to dd page
        Then import patents
        Then start analysis

    Scenario: tech1
        Given on workspace
        Then wait for tech1
        Then change tech1 select data
        Then download tech1 pdf
        Then validate customized tech1

    Scenario: tech2 class
        Given on workspace
        Then wait for tech2
        Then change tech2 class select data
        Then download tech2 pdf
        Then validate customized tech2 class

    Scenario: tech2 subclass
        Given on workspace
        Then wait for tech2
        Then change tech2 subclass select data
        Then download tech2 pdf
        Then validate customized tech2 subclass

    Scenario: tech2 group
        Given on workspace
        Then wait for tech2
        Then change tech2 group select data
        Then download tech2 pdf
        Then validate customized tech2 group

    Scenario: tech2 subgroup
        Given on workspace
        Then wait for tech2
        Then change tech2 subgroup select data
        Then download tech2 pdf
        Then validate customized tech2 subgroup

    Scenario: oi2 inventors
        Given on workspace
        Then wait for oi2
        Then change oi2 inventors select data
        Then download oi2 inventors pdf
        Then validate customized oi2 inventors

    Scenario: oi2 applicants
        Given on workspace
        Then wait for oi2
        Then change oi2 applicants select data
        Then download oi2 assignees pdf
        Then validate customized oi2 assignees

    Scenario: oi3
        Given on workspace
        Then wait for oi3
        Then change oi3 select data
        Then download oi3 pdf
        Then validate customized oi3

    Scenario: hh1
        Given on workspace
        Then wait for hh1
        Then change hh1 select data
        Then download hh1 transferred pdf
        Then validate customized hh1 transferred

    Scenario: vh1
        Given on workspace
        Then wait for vh1
        Then change vh1 select data
        Then download vh1 quantity pdf
        Then validate customized vh1

    Scenario: vh2
        Given on workspace
        Then wait for vh2
        Then change vh2 select data
        Then download vh2 pdf
        Then validate customized vh2

    Scenario: vh3 potential targets
        Given on workspace
        Then wait for vh3
        Then change vh3 family id select data
        Then download vh3 potential targets pdf
        Then validate customized vh3 potential targets
        Then change vh3 potential targets select data
        Then download vh3 potential targets pdf
        Then validate customized vh3 potential targets

    Scenario: vh3 family id
        Given on workspace
        Then wait for vh3
        Then vh3 switch to family id tab
        Then wait for vh3
        Then change vh3 potential targets select data
        Then download vh3 family id pdf
        Then validate customized vh3 family id
        Then change vh3 family id select data
        Then download vh3 family id pdf
        Then validate customized vh3 family id