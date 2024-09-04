def search_and_replace(text2, search_word, replace_word):
    try:
       with open(r'text2.txt') as fileObj:
            content = fileObj.read()
            newContent = content.replace(search_word, replace_word)

            with open(r'text2.txt','w') as fileObj:
                fileObj.write("Hello Alisha")

                print("All occurrences of ", search_word, "replaced with ", replace_word)

    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: Unable to read or write to the file.")
    except Exception as e:
        print("An unexpected error occurred: ", e)

search_and_replace('text2.txt', 'hello', 'hi')