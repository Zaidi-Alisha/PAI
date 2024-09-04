def lists_to_dict(list1, list2, text3):
    try:
        if len(list1) != len(list2):
            raise ValueError("Both lists must have the same number of elements.")

        dictionary = {list1[i]: list2[i] for i in range(len(list1))}

        with open(text3, 'w') as fileObj:
            for key, value in dictionary.items():
                fileObj.write(key)

        print("Dictionary created and saved to ", text3)
    except ValueError as ve:
        print("ValueError: ", ve)
    except IOError:
        print("Error: Unable to write to the file.")
    except Exception as e:
        print("An unexpected error occurred: ", e)


list1 = ['Alisha', 'Sarim', 'Mehak']
list2 = ['Computer', 'English', 'Mathematics']
lists_to_dict(list1, list2, 'text3.txt')