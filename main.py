def convert_kg_to_lbs(weight_in_kg):
    result = weight_in_kg * 2.20462
    return result


def convert_lbs_tokg(weight_in_lbs):
    result = weight_in_lbs / 2.20462
    return result


weight = input(
    "Type 1 to convert from pounds to kilos or 2 to convert from kilos to pounds: ")
if weight == "1":
    print(weight_in_lbs=weight_in_kg * 2.20462)
elif weight == "2":
    print(weight_in_kg=weight_in_lbs / 2.20462)
else:
    print("Invalid, please pick 1 or 2.")


weight_in_kg = float(input("Enter weight in KG: "))
weight_in_lbs = weight_in_kg * 2.20462
print(weight_in_lbs)

weight_in_lbs = float(input("Enter weight in LBS: "))
weight_in_kg = weight_in_lbs / 2.20462
print(weight_in_kg)


user_kg = float(input("Enter kilograms to convert: "))
final_lbs = convert_kg_to_lbs(user_kg)
print(f"That is equal to {final_lbs} lbs!")

user_lbs = float(input("Enter pounds to convert: "))
final_kg = convert_lbs_to_kg(user_lbs)
print(f"That is equal to {final_kg} kg!")
