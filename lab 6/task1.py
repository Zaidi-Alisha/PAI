def count(text1):
    try:
        with open(r'text1.txt') as fileObj:
            content = fileObj.read()
            characters = len(content)
            words = len(content.split())
            print("Total characters: ", characters)
            print("Total words: ", words)
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Cannot read file.")
    except Exception as e:
        print("An unexpected error occurred: ", e)


count('text.txt')