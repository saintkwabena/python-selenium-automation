## Created by isaac at 10/11/2024
Feature: Tests for Target Search functionality

  Scenario: User can search for coffee
    Given Open target main page
    When Search for a coffee
    Then Verify that correct search results shown for coffee
    Then Verify product coffee in URL


Scenario: User can search for a tea
    Given Open target main page
    When Search for a tea
    Then Verify that correct search results shown for tea

#
Scenario Outline: User can search for product
    Given Open target main page
    When Search for <search_word>
    Then Verify that correct search results shown for <search_result>
    Examples:
    |search_word  |search_result |
    |coffee       |coffee        |
    |tea          |tea           |
    |mug          |mug           |
    |sugar        |sugar         |

  Scenario: User can add a product to cart
    Given Open target main page
    When Search for mug
    And Click on Add to Cart button
    And  Store product name
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product


  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image


  Scenario: Verify user can access Sign in
    Given Open target main page
    When Click sign In
    And Click Sign In from right navigation
    Then Verify Sign In form opened









  Scenario: User can see favorites tooltip for search results
    Given Open Target main page
    When Search for tea
    And Hover favorites icon
    Then Favorites tooltip is shown



