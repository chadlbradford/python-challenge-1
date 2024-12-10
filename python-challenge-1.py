#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order = []



# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")


            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            
            # 2. Ask customer to input menu item number
            menu_item_number = input("Please enter a menu item number: ")

            # 3. Check if the customer typed a number
            # Check if the input is numeric
            if menu_item_number.isdigit():
                menu_item_number = int(menu_item_number)  # Convert to integer
                # Check if the number is a valid menu item
                if menu_item_number in menu_items.keys():
                    # Proceed with valid menu item
                    pass
                else:
                    print("Invalid menu item number.")
            else:
                print("Please enter a valid number.")
                
            # 4. Check if the menu selection is in the menu items
            # Check if the menu selection is in the menu items
            if menu_item_number in menu_items:
                # Retrieve the selected item details
                selected_item = menu_items[menu_item_number]
                item_name = selected_item["Item name"]
                item_price = selected_item["Price"]
                print(f"You selected: {item_name} - ${item_price:.2f}")
            else:
                print("Invalid selection. Please choose a valid menu item number.")
                
                # Store the item name as a variable
                # Retrieve the selected item details
                selected_item = menu_items[menu_item_number]  # Get the dictionary for the selected item
                item_name = selected_item["Item name"]        # Store the item name as a variable

            # Ask the customer for the quantity of the menu item
            quantity = input(f"How many {item_name} would you like to order? ").strip()

            # Check if the quantity is a number, default to 1 if not
            if quantity.isdigit() and int(quantity) > 0:
                quantity = int(quantity)  # Convert quantity to an integer
                print(f"You have ordered {quantity} x {item_name}.")

                # Add the item name, price, and quantity to the order list
                
                order.append({
                    "name": item_name,
                    "price": item_price,
                    "quantity": quantity
                })
                print("Item added to your order!")
            # Tell the customer that their input isn't valid

            else:
                print("Invalid selection. Please choose a valid menu item number.")

 
    # Tell the customer they didn't select a menu option

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")


        # 5. Check the customer's input
        # Keep ordering
        if keep_ordering == "Y":
            print("\nGreat! Let's continue your order.")
            break  # Exit the loop and continue ordering
        
        # Exit the keep ordering question loop
        elif keep_ordering == "N":
            print("\nThanks for ordering!  Completing your order...")
            place_order = False  # Exit the main ordering loop
            break
        else:
            print("Invalid input. Please enter 'Y' for yes or 'N' for no.")
            

            # Complete the order

            # Since the customer decided to stop ordering, thank them for
            # their order
                


            # Exit the keep ordering question loop


            # Tell the customer to try again


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("\nYour Order Summary:")
print("Item name                | Price  | Quantity | Subtotal")
print("-------------------------|--------|----------|---------")
total_cost = 0
for item in order:
    subtotal = item["price"] * item["quantity"]  # Calculate the subtotal
    total_cost += subtotal  # Add the subtotal to the total cost
    num_item_spaces = 24 - len(item["name"])  # Calculate spacing for alignment
    item_spaces = " " * num_item_spaces  # Create the spacing string
    # Print the formatted line for the item
    print(f"{item['name']}{item_spaces} | ${item['price']:.2f}  | {item['quantity']}        | ${subtotal:.2f}")

# 6. Loop through the items in the customer's order
for item in order:
    # 7. Store the dictionary items as variables
    item_name = item["name"]
    item_price = item["price"]
    item_quantity = item["quantity"]

    
    # 8. Calculate the number of spaces for formatted printing

    # 9. Create space strings

    # 10. Print the item name, price, and quantity


# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
total_cost = sum(item["price"] * item["quantity"] for item in order)

# Print the total cost
print(f"Total cost of your order: ${total_cost:.2f}")


