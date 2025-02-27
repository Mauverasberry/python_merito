*** Settings ***
Library    SeleniumLibrary     #importuje biblioteke selenium, która pozwala sterować przeglądarką w testach automatycznych.
# w momencie jak zaczynasz jakikolwiek test wykonaj:
Test Setup    open browser    https://pl.wikipedia.org    chrome
Test Teardown    close browser     # Po zakończeniu testu zamyka przeglądarkę.

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
    click element    wpLoginAttempt                 #Kliknięcie w przycisk „Zaloguj się”.
    sleep    1
    #capture page screenshot    screen.png    #robi screena i napisuje screena
    # czekaj aż pojawi się element błędu logowania.
    wait until element is visible   xpath:/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[3]/div/form/div[1]/div
    # Pobiera komunikat błędu i zapisuje go do zmiennej ${my error message}.
    ${my error message}    get text    xpath:/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[3]/div/form/div[1]/div
    log to console    Wiadomosc: ${my error message}    #wiadomosc na konsoli zamiast print
    should be equal    ${my error message}    ${error message}    #Sprawdza, czy otrzymany komunikat błędu jest zgodny z oczekiwanym.

*** Test Cases ***
#Test nieudanego logowania
Unsuccesfull login
    Log in wikipedia
#Test wyszukiwania na Wikipedii
Wikipedia search
    Log in wikipedia    #wrzuca wszytsko z Keyworks
    input text    search    Kto rządzi w Warszawie i okolicach    False    #false nie czysci okna bnez sensu ale pokazowe
    capture page screenshot    screen.png       #Zapisuje zrzut ekranu strony.
    close browser
# uruchamianie pliku - wpisanie w terminalu -    robot .\7_robot_basic.robot