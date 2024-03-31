
# # Create an empty list to store a customer's order in dictionary format
order_list = [
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
]
#Print the order list to see the structure 
print(order_list)

# Menu dictionary
menu_sections = {
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

#Print the order list to see the structure 
print(menu_sections)

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = [
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
]


# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")
print("How can we assist you today")

menu_selection = input ("Please enter your selection from the menu: ")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")
    # Check the customer's response to continue or end the orderin
    if keep_ordering.lower() == 'n': 
        place_order = False
        print("Thank you for your order!")
    elif keep_ordering.lower() != 'y':
        print("Invalid input. Please try again.")

    # Create a variable for the menu item number
    i = 1
    
    # Check if the user input is a number
    try:
        menu_selection = int(menu_selection)  # Convert the input to an integer
        # Check if the converted input is in the keys of menu_items
        if menu_selection in menu_items.keys():
            # Continue with further processing
            # Get the item name from the menu_items dictionary and store it as a variable
            item_name = menu_items[menu_selection]
        else:
            print("Error: Your selection is not in the menu items.")
    except ValueError:
        print("Error: You must enter a number.")


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
            menu_selection = int(input("Please enter the number of the menu item you would like to order: "))

            # 3. Check if the customer typed a number
            user_input = input("Please enter a number: ")

            if user_input.isdigit():
                print("The input is a number.")
            else:
                print("The input is not a number.") 

                # Convert the menu selection to an integer
                menu_selection = int(input("Please enter the number of the menu item you would like to order: "))

                # 4. Check if the menu selection is in the menu items
                menu_items = {1: "Pizza", 2: "Burger", 3: "Cookie"}  # Example menu items dictionary

                menu_selection = 2  # Example menu selection

                if menu_selection in menu_items:
                    print("Menu selection is valid.")
                else:
                    print("Menu selection is not valid.")

                    # Store the item name as a variable
                    menu_items = {1: "Pizza", 2: "Burger", 3: "Cookie"}  # Example menu items dictionary

                    menu_selection = 2  # Example menu selection

                    if menu_selection in menu_items:
                    print("Menu selection is valid.")
                    else:
                        print("Menu selection is not valid.")   
                    
                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"How many {item_name}s would you like? (Quantity will default to 1 if input is invalid): ")

                    # Check if the quantity input is a number
                    if not quantity.isdigit():
                        print("Invalid input. Defaulting quantity to 1.")
                        quantity = 1
                    else:
                        quantity = int(quantity)

                    # Add the item name, price, and quantity to the order list
                    order_list = []

                    # Assume these are the item details
                    item_name = "Burger"
                    price = 8.49
                    quantity = 2

                    # Create a dictionary for the item
                    item_dict = {
                        "item_name": item_name,
                        "price": price,
                        "quantity": quantity
                    }

                    # Add the item dictionary to the order list
                    order_list.append(item_dict)

                    print("Item added to the order list:")
                    print(order_list)

                    # Tell the customer that their input isn't valid
                    print("Your input is not valid. Please enter a valid menu item number.")

                # Tell the customer they didn't select a menu option
                print("You did not select a valid menu option. Please choose a valid menu item number.")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number. Please enter a valid number for the menu item.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        menu_items = {1: "Pizza", 2: "Burger", 3: "Salad"}  # Example menu items dictionary

        user_input = input("Please enter the number of the menu item you would like to order: ")

        if user_input.isdigit():
         menu_selection = int(user_input)
        if menu_selection in menu_items:
            item_name = menu_items[menu_selection]
            print("You selected:", item_name)
            # Add the item name, price, and quantity to the order list here
        else:
            print("You did not select a valid menu option. Please choose a valid menu item number.")
        else:
            print("You didn't select a number. Please enter a valid number for the menu item.")
                # Keep ordering
                menu = {
                    1: "Pizza",
                    2: "Burger",
                    3: "Salad"
                }

                orders = []

                while True:
                    print("Menu:")
                    for item in menu:
                        print(f"{item}: {menu[item]}")

                    choice = int(input("Enter the number of the item you want to order: "))
                    if choice in menu:
                        orders.append(menu[choice])
                     else:
                        print("Invalid choice. Please try again.")

                    another_order = input("Do you want to order another item? (y/n): ")
                    if another_order.lower() != 'y':
                        break

                print("Your orders:")
                for order in orders:
                     print(order)

                # Exit the keep ordering question loop
                place_order = True

                while place_order:
                    # Your code for ordering goes here
                    user_input = input("Do you want to place another order? (yes/no): ")
    
                     if user_input.lower() != "yes":
                        place_order = False  # Set the condition to False to exit the loop
                        print("Exiting the ordering loop.")

                # Complete the order

                # Since the customer decided to stop ordering, thank them for
                # their order

                # Exit the keep ordering question loop


                # Tell the customer to try again


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order

    # 7. Store the dictionary items as variables


    # 8. Calculate the number of spaces for formatted printing


    # 9. Create space strings


    # 10. Print the item name, price, and quantity


# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
