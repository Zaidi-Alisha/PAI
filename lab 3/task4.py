def save_biodata(text4):
    try:
        name = input("Enter Name: ")
        cnic = input("Enter CNIC Number: ")
        age = input("Enter Age: ")
        salary = input("Enter Salary: ")

        with open("text4.txt", 'w') as fileObj:
            fileObj.write(f"Name: {name}\n")
            fileObj.write(f"CNIC: {cnic}\n")
            fileObj.write(f"Age: {age}\n")
            fileObj.write(f"Salary: {salary}\n")

        print("Biodata saved.")

        contact = input("Enter Contact Number: ")
        with open(text4, 'a') as fileObj:
            fileObj.write(f"Contact Number: {contact}\n")

        print("Contact number changed.")
        with open(text4, 'r') as fileObj:
            content = fileObj.read()
            print("File content:")
            print(content)

    except IOError:
        print("Error: Unable to write to or read the file.")
    except Exception as e:
        print("An unexpected error occurred: ", e)


save_biodata('text4.txt')