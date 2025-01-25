*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${wikipedia login}    RobotTests
${wikipedia password}    RobotFramework
*** Keywords ***

*** Test Cases ***
Log in wikipedia
    open browser    https://pl.wikipedia.org     chrome
    click element     pt-login-2
    sleep      1
    input text    wpName1     ${wikipedia login}
    input text    wpPassword1    ${wikipedia password}
    sleep    1
    click element    wpLoginAttempt
    sleep    1
    capture page screenshot    screen.png
    close browser


Wikipedia search
    open browser    https://pl.wikipedia.org     chrome
    click element     pt-login-2
    sleep      1
    input text    wpName1     ${wikipedia login}
    input text    wpPassword1    ${wikipedia password}
    sleep    1
    click element    wpLoginAttempt
    sleep    1
    input text    searchInput    Kto żądzi w Warszawie i okolicach    False
    capture page screenshot    screen.png
    close browser