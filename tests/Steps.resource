*** Settings ***
Library    SeleniumLibrary
Library    Tile.py    WITH NAME    tile

*** Keywords ***
user is in ${expression} and tile selection count is 0
    ${url} =   Get Location
    ${selection_count} =    Get Selection Count
    Should Be Equal    ${expression}    ${url}
    Should Be Equal    ${selection_count}    ${0}

user selects the tile number ${expression} and the tile color is ${expected_color}
    Create Selector    ${expression}
    ${selector} =  Get Selector
    ${class} =    Get Element Attribute    ${selector}        class
    Set Tile Color    ${class}
    ${color} =    Get Tile Color
    Should Be Equal    ${color}    ${expected_color}
    Click Element    ${selector}
    ${class} =    Get Element Attribute    ${selector}        class
    Set Tile Color    ${class}
    ${set_color} =    Get Tile Color

    IF  "${set_color}" == "green"
        Add To Selection Count
    ELSE IF  "${set_color}" == "white"
        Remove From Selection Count
    END

the tile number ${expression} is selected and its color is ${expected_color}
    Create Selector    ${expression}
    ${selector} =  Get Selector
    ${class} =    Get Element Attribute    ${selector}        class
    ${color} =    Get Tile Color
    Should Be Equal    ${color}    ${expected_color}