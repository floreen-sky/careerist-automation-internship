# Created by Flo at 4/5/2021
Feature: GetTop Category Page

  Scenario: Verify items to correct category
    Given Open GetTop Page
    When Navigate to iPhone Category
    Then Verify all Items Category

  Scenario: Verify number of Items
    Given Open GetTop Page
    When Navigate to iPhone Category
    Then Verify number of Items

  Scenario: Verify Category, Name and Price
    Given Open GetTop Page
    When Navigate to iPhone Category
    Then  Verify every Item Category, Name and Price

  Scenario: Open and close Quick View
    Given Open GetTop Page
    When Navigate to iPhone Category
    Then Hover on Item Picture
    And Click on Quick View Button
    And Close the Quick View

  Scenario: Open Quick View and add Item to Cart
    Given Open GetTop Page
    When Navigate to iPhone Category
    Then Hover on Item Picture
    And Click on Quick View Button
    Then Add Item to Cart