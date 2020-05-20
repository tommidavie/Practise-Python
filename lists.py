import random
# Just for the shuffle 

def get_integer(m):
    my_integer = int(input(m))
    return my_integer

def get_string(m):
    my_string = input(m)
    return my_string

def print_at_index(L):
    my_index = get_integer("Please choose index -> ")
    print(L[my_index])

def print_list(L):
    for x in L:
        print(x)

def print_list_indexes(L):
    for i in range (0, len(L)):
        print("{} : {}".format(i, L[i]))

def add_item(L):
    new_item = get_string("Please enter new item: ")
    L.append(new_item)

def change_value(L):
    
    print_list_indexes(L)
    index_num = get_integer("Please choose the index number: ")
    new_value = get_string("Please enter new value: ")
    # we now have all the values we need
    # temporarily hold old value for print out
    old_value = L[index_num]
    # update value
    L[index_num]=new_value
    # confirmation message
    output = "The old value of {} has now been changed to {}".format(old_value, L[index_num])
    print(output)

def remove_item(L):

    item = get_string("What do you want to remove: ")
    if item in L:
        L.remove(item)
        output = "{} has been removed from the list.".format(item)
        print(output)
    else:
        output = "{} could not be found, so must have not been in the list".format(item)
        print(output)

def sort_list(L):
    L.sort()
 
def shuffle_list(L):
    random.shuffle(L)

def find_item(L):
    item = get_string("What do you want to find? : ")
    if item in L:
        index_num = L.index(item)
        output = "{} has been found at an index number of {}".format(L[index_num], index_num)
        print(output)                     
    else:
        print("{} cannot be found in the list".format(item))
        print("."*100)

def menu():
    my_list_one=["Tommi", "Grace", "Paige", "Rebecca", "Nia"]
    my_list_two=["Mango", "Apple", "Pear", "Orange", "Banana"]
    my_list = my_list_two

    my_menu = '''
    A: Print the list
    B: Print the list with indices
    C: Add item to the list
    D: Print at index number
    E: Choose list one
    F: Choose list two
    G: Change a Value
    H: Remove an Item
    I: Sort a list
    J: Shuffle a list
    L: Find an item
    Q: Quit
    '''

    print(id(my_list_one))
    print(id(my_list_two))
    print(id(my_list))

    run = True
    while run == True:
        print(my_menu)
        ask = get_string("Please select an option: ")
        print("."*100)
        if ask == "A":
            print_list(my_list)
        elif ask == "B":
            print_list_indexes(my_list)
        elif ask == "C":
            add_item(my_list)
        elif ask == "D":
            print_at_index(my_list)
        elif ask == "E":
            my_list = my_list_one
            print("My list one is now selected")
        elif ask == "F":
            my_list = my_list_two
            print("My list two is now selected")
        elif ask == "G":
            change_value(my_list)
        elif ask == "H":
            remove_item(my_list)
        elif ask == "I":
            sort_list(my_list)
        elif ask == "J":
            shuffle_list(my_list)
        elif ask == "L":
            find_item(my_list)
        elif ask == "Q":
            print("Thank you for playing")
            run = False

menu()

#print_at_index(my_list) 
#print_list(my_list)
#print_list_indexes(my_list)
#add_item(my_list)

