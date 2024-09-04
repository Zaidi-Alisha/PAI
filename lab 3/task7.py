def replace_letter(replacement='replacement.txt', letter='h', replaced='n'):
    try:
        with open(replacement, 'r') as fileObj:
            content = fileObj.read()

        if letter in content:
            content = content.replace(letter, replaced)

        with open(replacement, 'w') as file:
            file.write(content)
        print(f"Replaced '{letter}' with '{replaced}' in {replacement}.")
    except FileNotFoundError:
        print("The file ", replacement, "was not found.")
    except Exception as e:
        print("An error occurred: ", e)


replace_letter('replacement.txt')

