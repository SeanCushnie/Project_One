# Project_One

BRIEF:
MVP:
1: The inventory should track individual products, including a name, description, stock quantity, buying cost, and selling price.
2: The inventory should track manufacturers, including a name and any other appropriate details.
3: The shop can sell anything you like, but you should be able to create and edit manufacturers and products separately
4: Show an inventory page, listing all the details for all the products in stock in a single view.
5: As well as showing stock quantity as a number, the app should visually highlight "low stock" and "out of stock" items to the user.
Extensions:
6: Calculate the markup on items in the store, and display it in the inventory
7: Filter the inventory list by manufacturer. For example, provide an option to view all books in stock by a certain author.
8: Categorise your items. Books might be categorised by genre (crime, horror, romance...) and cars might be categorised by type (SUV, coupé, hatchback...). Provide an option to filter the inventory list by these categories.
9: Mark manufacturers as active/deactivated. Deactivated manufacturers will not appear when creating new products.

Checklist (Brief points that I've been able to successfully implement):
1: YES
2: YES
3: YES
4: YES
5: YES
6: YES
7: YES
8: NO
9: MAYBE: When manufacturer is deleted, you can no longer select them as an option when adding a new product. 

INSTRUCTIONS FOR USE:
IN TERMINAL, TYPE (excluding "" and hitting ENTER, after inputting every line):
1: "DROPDB products_controller"
2: "CREATEDB products_controller"
3: "psql -d products_manager -f db/products_manager.sql"
4: "python3 console.py"
5: "flask run"
6: hold COMMAND and CLICK on http://127.0.0.1:4999

ON WEBPAGE:
PRODUCTS:
1. CLICK "products" to view the list of products and their corresponding details.
2. CLICK "EDIT PRODUCT" to change the product. Be sure to input all relevant details.
3. CLICK the bin to delete the product. 
MANUFACTURERS:
1. CLICK "manufacturers" to view the list of manufacturers.
2. CLICK "view *manufacturer* products" to view the list of products specific to the manufacturer. 
3. CLICK "EDIT MANUFACTURER" to change the manufacturer. Be sure to input all relevant details.
4. CLICK the bin to delete the manufacturer.
ADDING PRODUCTS:
1. CLICK "add products" to begin the process of appending the list of products with a new one.
2. Select the manufacturer and input all relevant details.
3. CLICK "Add Product"
ADDING MANUFACTURERS:
1. CLICK "add manufacturer" to begin the process of appending the list of manufacturers with a new one.
2. Input a name 
3. CLICK 'add manufacturer' below the input field.
