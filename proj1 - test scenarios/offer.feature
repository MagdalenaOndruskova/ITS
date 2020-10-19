Feature: Offer of products 

Scenario: Show product from homepage
Given a web browser is at e-shop homepage
When customer clicks on "MacBook"
Then page with product details is shown 


Scenario: Search product from search bar 
Given a web browser is at e-shop homepage 
When customer searchs "MacBook"
Then page with following products is shown:
        | product     |
        | MacBook     |
        | MacBook Air |
        | MacBook Pro |


Scenario: Show not-empty category 
Given a web browser is at e-shop homepage 
When customer clicks on "Phones & PDAs"
Then page with following products are shown:
        | product       | 
        | HTC Touch HD  | 
        | iPhone        |
        | Palm Tree Pro |


Scenario: Show empty category
Given a web browser is at e-shop homepage
When customer clicks on "Software"
Then customer is shown text: "There are no products to list in this category."


Scenario: Show subcategory list 
Given a web browser is at e-shop homepage 
When customer clicks on "Desktop"
Then dropmenu is shown containing subcategories:
        | subcategory  |
        | PC           |
        | Mac          |


Scenario: Show not-empty subcategory
Given a web browser is at e-shop homepage 
And "Desktop" dropmenu is shown 
When customer clicks on "Mac"
Then page with following products is shown:
        | product     |
        | iMac        |


Scenario: Show empty subcategory 
Given a web browser is at e-shop homepage
And "Desktop" dropmenu is shown 
When customer clicks on "PC"
Then customer is shown text: "There are no products to list in this category."

