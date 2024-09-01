def create(list1, list2):
    new_dict = {} 
    
    for i in range(len(list1)):
        new_dict[list1[i]] = list2[i] 
    
    return new_dict

def main():
    list1 = input("Enter the elements of list 1: ").split()
    
    list2 = input("Enter the elements of list 2: ").split()
    
    if len(list1) != len(list2):
        print("The lists must have the same number of elements.")
        return
    
    new_dict = create(list1, list2)
    
    print("RThis is the dictionary:", new_dict)

if __name__ == "__main__":
    main()
