Feature: Customer informations

Scenario: Customer account options
Given a web browser is at e-shop homepage 
When customer clicks on "My account"
Then dropmenu is shown containing subcategories: 
        | subcategory   | 
        | Register      |
        | Login         |


Scenario Outline: Registration of new customer - Without filling required fields 
Given a web browser is at registration page
And <required> fields are empty 
When customer clicks on "Continue"
Then warnings bellow <required> fields are displayed 
    Examples: Required fields
    | required        |
    | First Name      |
    | Last Name       |
    | E-Mail          | 
    | Telephone       | 
    | Adress 1        | 
    | City            | 
    | Post Code       |
    | Region / State  |
    | Password        |


Scenario: Registration of new customer - Not agreeing to Privacy Policy
Given a web browser is at registration page
And required fields are filled 
When customer clicks on "Continue"
Then a warning is shown: "Warning: You must agree to the Privacy Policy!"


Scenario: Registration of new customer - Valid registration 
Given a web browser is at registration page
And required fields are filled
And "I have read and agree to the Privacy Policy" box is ticked 
When customer clicks on "Continue"
Then customer is shown:  "Your Account Has Been Created!"


Scenario: Account options 
Given a web browser is at e-shop homepage
And customer is logged in 
And dropmenu for "My Account" is shown
When customer clicks on "My Account"
Then customer is shown actions with his account:
        | actions                                | 
        | Edit your account information          |
        | Change your password                   |
        | Modify your address book entries       |
        | Modify your wish list                  |
        | View your order history                | 
        | Downloads                              |
        | Your Reward Points                     |
        | View your return requests              |
        | Your Transactions                      |
        | Recurring payments                     |
        | Subscribe / unsusbscribe to newsletter |


Scenario: Display personal information 
Given a web browser is at "My Account" page 
When customer clicks on "Edit your account information"
Then page with your_personal_details is shown with filled_fields:
    | your_personal_details | filled_fields   |
    | First Name            | Magdalena       |
    | Last Name             | Ondruskova      | 
    | E-Mail                | email@gmail.com |
    | Telephone             | 12345872        |
    | Fax                   |                 |


Scenario Outline: Edit personal information 
Given a web browser is at "My Account Information" page
And <your_personal_details> is changed to <new_personal_details>
When customer clicks on "Continue "
Then customer is shown page: " Success: Your account has been successfully updated."
    Examples: Personal details update
    | your_personal_details      | new_personal_details     |
    | Magdalena                  | Patricia                 |
    | Ondruskova                 | Ondrusova                |
    | email@gmail.com            | new@gmail.com            | 
    | 12345872                   | 0235879                  |


Scenario: Delete existing address
Given a web browser is at "Address Book Entries" page
And only one address is filled 
When customer clicks on "Delete"
Then customer is shown: "Warning: You can not delete your default address!" 


Scenario Outline: Edit existing address
Given a web browser is at "Address Book Entries" page
When customer clicks on <button>
Then "Edit Adress" page is shown 
    Examples:
    | button      |
    | Edit        |
    | New address |


Scenario Outline: Edit existing address
Given a web browser is at "Edit Address" page
And <address_filled> is changed to <new_address>
When customer clicks on "Continue"
Then to customer is shown: "Your address has been successfully updated"
    Examples: Changing address
    | address_filled    | new_address    |
    | Magdalena         | Majdalena      |
    | Ondruskova        | Ondrusova      |
    | TuByvam 325       | Nova Ulica 22  | 
    | Mesto             | Nove Mesto     |
    | 98798             |                |
    | Slovak Republic   | Czech Republic |
    | Trnavský          | Bratislavský   |


Scenario: Deleting address
Given a web browser is at "Address Book Entries" page
And more than one address is filled 
When customer clicks on "Delete"
Then customer is shown: " Your address has been successfully deleted" 


Scenario: Edit subscription to newsletter
Given a web browser is at "My Account" page
When customer clicks on "Subscribe / unsusbscribe to newsletter"
Then customer is shown page: "Newsletter Subscription"


Scenario Outline: Edit subscription to newsletter
Given a web browser is at "Newsletter Subscription" page
And customer clicks on <button>
When customer clicks on "Continue"
Then customer is shown:  Success: "Your newsletter subscription has been successfully updated!"
    Examples:
    | button  | 
    | Yes     |
    | No      |
    

Scenario: Logging-out 
Given a web browser is at e-shop homepage
And dropmenu for "My Account" is shown
When customer clicks on "Logout"
Then customer is shown page: "Account Logout"
 