*** Settings ***
Library    SeleniumLibrary     #importuje biblioteke selenium
# w momencie jak zaczynasz jakikolwiek test wykonaj:
Test Setup    open browser    https://pl.wikipedia.org    chrome
Test Teardown    close browser

*** Variables ***
#zmienna int albo string ${ w ten sposob definiujemy
${wikipedia login}  RobotTests
${wikipedia_password}    azaa    # RobotFramework    - specjalnie zle haslo
${error_message}    Podany login lub haslo są nieprawidłowe. Spróbuj jeszcze raz

*** Keywords ***
Log in wikipedia    #nazwa testu
    click element    pt-login-2     #klika element zaloguj (ryc.1)
    sleep    1
    input text    wpName1    ${wikipedia login}     #wpisuje nazwę urzytkownika (ryc.2)
    input text    wpPassword1    ${wikipedia_password}
    sleep    1
    click element    wpLoginAttempt
    sleep    1
    #capture page screenshot    screen.png    #robi screena i napisuje screena
    # czekaj az element bedzie widoczny
    wait until element is visible   xpath:/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[3]/div/form/div[1]/div
    # przechwyc tekst z tego full xpath
    ${my error message}    get text    xpath:/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[3]/div/form/div[1]/div
    log to console    Wiadomosc: ${my error message}    #wiadomosc na konsoli zamiast print
    should be equal    ${my error message}    ${error message}    #czy jest równe

*** Test Cases ***

Unsuccesfull login
    Log in wikipedia

Wikipedia search
    Log in wikipedia    #wrzuca wszytsko z Keyworks
    input text    search    Kto rządzi w Warszawie i okolicach    False    #false nie czysci okna bnez sensu ale pokazowe
    capture page screenshot    screen.png
    close browser
