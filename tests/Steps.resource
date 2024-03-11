*** Settings ***
Library    SeleniumLibrary
Library    Tile.py    WITH NAME    tile

*** Keywords ***
user is in ${expression} and tile selection count is 0
    ${url} =   Get Location
    ${selection_count} =    Get Selection Count
    Should Be Equal    ${expression}    ${url}
    Should Be Equal    ${selection_count}    ${0}

user selects the tile number ${expression} and the tile color is white
    Create Selector    ${expression}
    ${selector} =  Get Selector
    ${class} =    Get Element Attribute    ${selector}        class
    Set Tile Color    ${class}
    ${color} =    Get Tile Color
    Should Be Equal    ${color}    white
    Click Element    ${selector}
    Add To Selection Count
    ${class} =    Get Element Attribute    ${selector}        class
    Set Tile Color    ${class}

the tile number ${expression} is selected and its color is green
    Create Selector    ${expression}
    ${selector} =  Get Selector
    ${class} =    Get Element Attribute    ${selector}        class
    ${color} =    Get Tile Color
    Should Be Equal    ${color}    green