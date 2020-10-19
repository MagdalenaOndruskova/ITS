Feature: Customer informations

Scenario: Customer account options
Given a web browser is at e-shop homepage 
When customer clicks on "My account"
Then user is shown the dropmenu My Account  with following subcategories:
        | MyAccountSub  |
        | Register      |
        | Login         |


Scenario Outline: Registration of new customer - Without filling required fields 
Given a web browser is at registration page
And <required> field is empty
When customer clicks on "Continue"
Then warnings bellow <required> field is displayed
    Examples: Required fields
    | required        |
    | First Name      |
    | Last Name       |
    | EMail          |
    | Telephone       |
    | Address 1        |
    | City            |
    | Post Code       |
    | Password        |


Scenario: Registration of new customer - Not agreeing to Privacy Policy
Given a web browser is at registration page
And required fields are filled
When customer clicks on "Continue"
Then a warning is shown: "Warning: You must agree to the Privacy Policy!"

