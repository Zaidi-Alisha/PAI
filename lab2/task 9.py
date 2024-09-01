def count_characters(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    num_characters = 0
    num_words = 0

    for char in text:
        num_characters += 1

    words = text.split()
    for word in words:
        num_words += 1

    print("Characters in this file:", num_characters)
    print("Words in this file:", num_words)

def main():
    file_path = input("Enter the path to the text file: ")
    count_characters(file_path)

if __name__ == "__main__":
    main()
