def print_list():
    """
    Prints the users list, with numbers to see.
    :return: No return, just directly prints the global variable user_list.
    """
    global user_list
    for i in range(len(user_list)):
        print(f"{i+1}. {user_list[i]}")



print("""
------------------------------------------------
    Welcome to the ultimate list making app!
""")

user_list = ["Milk", "Eggs", "Bread"]

while True:
    print("""
What would you like to do?

1. Add an item
2. Remove an item
3. Display the current list
4. Undo the previous change
5. Exit the program
    """)

    acceptable = [1, 2, 3, 4, 5]

    while True:
        try:
            user_choice = int(input("Please enter your choice: "))

            if user_choice not in acceptable:
                print("Please enter one of the 5 choices. ")
            else:
                break
        except ValueError:
            print("Please enter an actual number. ")

    if user_choice == 1:
        copied_list = user_list.copy()
        add_to_list = input("What would you like to add? ")
        user_list.append(add_to_list)
    elif user_choice == 2:
        if len(user_list) > 0:
            copied_list = user_list.copy()
            print("This is your list:")
            print_list()
            while True:
                try:
                    user_choice = int(input("What would you like to remove? Enter the number next to the item on the list. "))

                    if 0 < user_choice < len(user_list):
                        print("Please enter one of the numbers. ")
                    else:
                        break
                except ValueError:
                    print("Please enter an actual number. ")

        else:
            print("There's nothing to remove!")


