## CREATED A SHOPPING LIST

shopping_list = []
unique_items = set()
items_info = {}
our_store_items = {"Orange":10, "Mango":5, "Apple":10, "Pear":4, "PawPaw":15, "Banana":8, "Strawberry":7}

## Use a while loop to create a menu of options for the user to add, remove, or view items from the list.
while True:
    print("""Shopping List Menu
          1. Add Item
          2. Remove Item
          3. View Items
          4. Exit
          """)
    
## Use the input() function to prompt the user to make a selection from the menu.

    user_choice = int(input("Select from the available options\n1\n2\n3\n4\n"))
## Use an if-elif-else block to determine the user's selection and perform the corresponding action.
    if user_choice == 1:
## If the user selects 'add', use the input() function to prompt the user to enter an item to add to the list. Use the range() function to limit the number of items that can be added to the list.
        print("Add Item Selected.")
        print("These are the items we have in our store currently")
        for item in our_store_items.keys():
            print(item)
        for i in range(5):
            item = input("Enter item: ").capitalize()
            if item in our_store_items:
                if item in unique_items:
                    print(f"{item} is already in shopping list")
                else:
                    item_quantity = int(input(f"How many quantity of {item}?: "))
                    shopping_list.append(item)
                unique_items.add(item)
                items_info[item] = item_quantity
                items_info[f"{item}_price"] = our_store_items[item]
                print(f"{item} has been added to your shopping cart")
            
            else:
                print("Sorry! We do not have this currently.")

    ## If the user selects 'remove', use the input() function to prompt the user to enter an item to remove from the list.
    elif user_choice == 2:
        item = input("Enter the item to remove: ")
        if items_info in shopping_list:
            shopping_list.remove(item)
            print(f"{item} has been removed..")
        
    ## If the user selects 'view', use a for loop to iterate through the list of items and display them to the user.
    elif user_choice == 3:
        print("Displaying items in your cart")
        if len(shopping_list) > 0:
            for item in shopping_list:
                print(f"{item} with {items_info[item]} quanity(s) with price of {items_info[f"{item}_price"]}")
        else:
            print("Your cart is empty")
    
    elif user_choice == 4:
        print("Thank you for patronizing us")
        break

    

