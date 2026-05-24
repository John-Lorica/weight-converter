# Input and if statements
weight = input(
    "Type 1 to convert from pounds to kilos or 2 to convert from kilos to pounds: ")
if weight == "1":
    print(lbs=kg * 2.20462)
elif weight == "2":
    print(kg=lbs / 2.20462)
else:
    print("Invalid, please pick 1 or 2.")


# Assignment operator
kilograms = float(input("Enter weight in KG: "))
pounds = kilograms * 2.20462
print(pounds)

pounds = float(input("Enter weight in LBS: "))
kilograms = pounds / 2.20462
print(kilograms)


# Definition and function
def convert_kg_to_lbs(weight_in_kg):
    result = weight_in_kg * 2.20462
    return result


user_kg = float(input("Enter kilograms to convert: "))
final_lbs = convert_kg_to_lbs(user_kg)
print(f"That is equal to {final_lbs} lbs!")

user_lbs = float(input("Enter pounds to convert: "))
final_kg = convert_lbs_to_kg(user_lbs)
print(f"That is equal to {final_kg} kg!")
