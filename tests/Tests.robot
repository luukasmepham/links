*** Settings ***
Documentation     Test Automation for the game Links

Library    SeleniumLibrary
Resource    Steps.resource
Variables    Variables.py

Test Setup     Open Browser    ${TestVariables.url}   ${TestVariables.browser}
Test Teardown  Close All Browsers

*** Test Cases ***
User selects a tile
    [tags]  smoke
    [Documentation]  User navigates into Links and selects the first tile of the grid
    Maximize Browser Window
    Given user is in ${TestVariables.url} and tile selection count is 0
    When user selects the tile number ${TestVariables.tile} and the tile color is white
    Then the tile number ${TestVariables.tile} is selected and its color is green