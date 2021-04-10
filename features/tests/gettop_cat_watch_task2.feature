# Created by Flo at 4/9/2021
Feature: GetTop Category Page - Watch

  Scenario: User can see all Items under WATCH Menu
    Given Open GetTop Page
    When Hover on Watch from Main Menu
    Then User can see all Items from dropdown Menu

  Scenario: User can open each Item under WATCH Menu and correct Pages open
    Given Open GetTop Page
    When  Hover on Watch from Main Menu
    Then  Verify if all Items open the correct Page