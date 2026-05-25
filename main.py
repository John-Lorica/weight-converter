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
