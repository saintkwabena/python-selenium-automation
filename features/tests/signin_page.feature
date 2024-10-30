# Created by isaac at 10/29/2024
Feature: Tests for Signin Page
  # Enter feature description here

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open sign in page
    And Store original window
    When Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And Close new window
    And switch back to original