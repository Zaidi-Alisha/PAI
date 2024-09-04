import json


def save_to_json(dictionary, data='data.json'):
    try:
        with open(data, 'w') as json_file:
            json.dump(dictionary, json_file)
        print(f"Dictionary saved to {data}.")
    except Exception as e:
        print("An error occurred: ", e)


dictionary = {'Ali': 23, 'Saad': 24, 'Salman': 15, 'Shams': 25, 'Sadiq': 46, 'Hammad': 23}
save_to_json(dictionary)


def load_from_json(data='data.json'):
    try:
        with open(data, 'r') as json_file:
            data = json.load(json_file)
        return data
    except Exception as e:
        print("An error occurred: ", e)
        return {}


def find_max(data):
    try:
        max_age = -1
        max_age_people = []
        for name, age in data.items():
            if age > max_age:
                max_age = age
                max_age_people = [name]
            elif age == max_age:
                max_age_people.append(name)

        print(f"Person(s) with the maximum age {max_age}: {', '.join(max_age_people)}")
    except Exception as e:
        print("An error occurred: ", e)


loaded_data = load_from_json()
find_max(loaded_data)