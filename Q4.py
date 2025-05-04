data = {
    "name": ["prince", "Dipu", "Akshay", "shyam"],
    "roll": [198, 111, 54, 248]
}

roll_dict = {}
for i in range(len(data["name"])):
    roll_dict[data["roll"][i]] = data["name"][i]

def search_by_roll(roll_number):
    return roll_dict.get(roll_number, "Roll number not found.")

roll_number_to_search = 248
print(search_by_roll(roll_number_to_search))

