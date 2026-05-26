choice = input("Type 1 to convert KG to LBS, or 2 to convert LBS to KG: ")


if choice == "1":
    print("You chose KG to LBS!")


elif choice == "2":
    print("You chose LBS to KG!")


else:
    print("Invalid choice! Please run the program again and type 1 or 2.")


def convert_kg_to_lbs(weight_in_kg):
    result = weight_in_kg * 2.20462
    return result


def convert_lbs_to_kg(weight_in_lbs):
    result = weight_in_lbs / 2.20462
    return result


user_kg = float(input("Enter kilograms to convert: "))
final_lbs = convert_kg_to_lbs(user_kg)
print(f"That is equal to {final_lbs} lbs!")

user_lbs = float(input("Enter pounds to convert: "))
final_kg = convert_lbs_to_kg(user_lbs)
print(f"That is equal to {final_kg} kg!")

# There needs to be an end here. Like, if you've already got your answer, it just ends.
