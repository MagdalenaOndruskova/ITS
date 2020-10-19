Feature: Offer of products

Scenario: Show product from homepage
Given a web browser is at e-shop homepage
When customer clicks on "MacBook"
Then page with product details is shown


Scenario: Search product from search bar
Given a web browser is at e-shop homepage
When customer searchs "MacBook"
Then page with MacBook products are shown:
        | product     |
        | MacBook     |
        | MacBook Air |
        | MacBook Pro |


Scenario: Show not-empty category
Given a web browser is at e-shop homepage
When customer clicks on "Phones & PDAs"
Then page with Phones & PDAs products are shown:
        | products       |
        | HTC Touch HD   |
        | iPhone         |
        | Palm Treo Pro  |

Scenario: Show empty category
Given a web browser is at e-shop homepage
When customer clicks on "Software"
Then customer is shown text: "There are no products to list in this category."


Scenario: Show subcategory list
Given a web browser is at e-shop homepage
When customer clicks on "Desktop"
Then dropmenu is shown containing subcategories:
        | subcategory  |
        | PC (0)       |
        | Mac (1)      |


Scenario: Show not-empty subcategory
Given a web browser is at e-shop homepage
And "Desktop" dropmenu is shown
When customer clicks on "Mac"
Then page with following Mac products is shown:
        | iMacProd    |
        | iMac        |


Scenario: Show empty subcategory
Given a web browser is at e-shop homepage
And "Desktop" dropmenu is shown
When customer clicks on "PC"
Then customer is shown text: "There are no products to list in this category."
