# Import the tabulate module
# please also import the module, otherwise the code will not run.

from tabulate import tabulate # type: ignore

# Create the menu list
menu = ["Coffee", "Grilled Beef Burger", "Gourmet Sandwhiches", "Green Salad"]

# Create the stock dictionary
stock = {'Coffee': 15,
            'Grilled Beef Burger': 10,
            'Gourmet Sandwhiches': 10,
            'Green Salad': 5}

# Create the price dictionary
price = {'Coffee': 35.99,
            'Grilled Beef Burger': 109.00,
            'Gourmet Sandwhiches': 85.00,
            'Green Salad': 69.90}

while True:
    # Create an empty list called "table"
    table = []
    # Map the items in the menu list to the ones in price dictionary
    # Add them to table
    for item in menu:
        table.append([f"{item:30} R{price[item]}"])

    # Create a header for printing the menu
    header = ["Cafe Menu"]
    # Center the header using center()
    centered_header = [header.center(35) for header in header]

    # Present the menu items in an organized table format utilizing the `tabulate()` method
    # Output the neatly formatted menu for display

    menu_table = tabulate(table, centered_header, tablefmt = 'simple_outline')
    print(menu_table)
    print()

    # Create an empty list named "item_value"
    item_value = []

    # Associate each item in the menu list with corresponding entries in the stock and price records
    # Determine **total_value** by multiplying the stock quantity by the item's price
    # Add the calculated values to the **item_value** list
    for item in menu:
        total_value = round((stock[item]) * (price[item]), 2)
        item_value.append([f"{item:40}", f"R{price[item]:.2f}", f"{stock[item]} units", f"R{total_value:.2f}"])

    # Create a list of headers to be displayed in table
    headers = ["Menu Item", "Price Per Item", "Available Stock", "Total Value"]

    # Exhibit the data in a structured format using the `tabulate()` function
    # Output the organized data for viewing
    item_value_table = tabulate(item_value, headers = headers, tablefmt = 'simple_outline')
    print(item_value_table)
    print()

    # Determine **total_stock** by adding up all individual stock amounts
    # Compute **total_price** by totaling the product of each item's price and its corresponding stock
    # Output the **total_stock** and **total_price** figures
    total_stock = sum(stock.values())
    total_price = sum(price[item] * stock[item] for item in menu)
    print(f"You have {total_stock} total stock with a combined value of R{total_price}.")
    
    # Ask the user if they want to add a new menu on the item
    add_new = input("Add a new menu item? (y/n) ").lower()

    # If the user chooses "n", close the program
    if add_new == "n":
        print("Thank you, Goodbye!")
        break
    
    # In case the user selects an option that is not recognized, prompt them to make another attempt
    # Return to the starting point for input

    elif add_new != "y":
        print("You have entered an invalid input. Please try again.")
        continue
    
    while True:
        # If the user selects "y", prompt them to input the name of the menu item
        # If the menu item is already in the system, ask the user to enter a different item
        if add_new == "y":
            new_item = input("Please enter the menu item: ").title()
            if new_item in menu:
                print("This item already exists. Please enter a new item.")
                continue
            
            # Reuqest user to enter the stock for the new item
            # Request user to enter the price of the new item
            new_stock = int(input(f"How many {new_item} do you have in stock? "))
            new_price = float(input(f"Please enter the price of each {new_item}: "))
            
            # Add the new item to the existing menu list
            # Refresh the inventory and pricing records with the latest items
            # Display a confirmation message for the user
            # Terminate the program
            menu.append(new_item)
            stock.update({new_item: new_stock})
            price.update({new_item: new_price})
            print(f"You have successfully added {new_stock} units of {new_item} at R{new_price}. Goodbye!")
            break