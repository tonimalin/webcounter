*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Counter can be set to given value
    Go To  ${HOME_URL}
    Title Should Be  Laskuri
    Input Text  value  5
    Click Button  Aseta
    Page Should Contain  nappia painettu 5 kertaa
