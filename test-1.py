# This is where I'll put the code I'm testing

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
