# 1. Ask the user for their choice
choice = input("Type 1 to convert KG to LBS, or 2 to convert LBS to KG: ")

# 2. Check the choice using an if/elif statement
if choice == "1":
    print("You chose KG to LBS!")
    # Your conversion math will go here

elif choice == "2":
    print("You chose LBS to KG!")
    # Your conversion math will go here

else:
    print("Invalid choice! Please run the program again and type 1 or 2.")
