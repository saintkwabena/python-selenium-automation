# Created by isaac at 10/29/2024
Feature: Tests for Signin Page
  # Enter feature description here

#  Scenario: User can open and close Terms and Conditions from sign in page
#    Given Open sign in page
#    And Store original window
#    When Click on Target terms and conditions link
#    And Switch to the newly opened window
#    Then Verify Terms and Conditions page is opened
#    And Close new window
#    And switch back to original


  Scenario: Sign in page with incorrect e-mail and password
    Given Open sign in page
    And incorrect email and password combination
    Then Clicks signin with password button
    And Verify that “Sorry, something went wrong. Please try again” message is shown