def get_integer(m):
    my_integer = int(input(m))
    return my_integer

def get_string(m):
    my_string = input(m)
    return my_string

def add_names_ages(N,A):
    count = get_integer("How many names and ages would you like: ")
    for i in range(0, count):
        names = get_string("Please enter your name: ")
        ages = get_integer("Please enter your age: ")
        N.append(names)
        A.append(ages)

def review(N,A):
    if len(N) == len(A):
        for i in range(0,len(N)):
            output = "{} is {} years old".format(N[i],A[i])
            print(output)
    else:
        print("An error has occured")
    
def menu():
    names = []
    ages = []

    my_menu = '''
    A: Add
    B: Review
    Q: Quit
    '''

    run = True
    while run == True:
        print(my_menu)
        ask = get_string("Please select an option: ")
        print("."*80)
        if ask == "A":
            add_names_ages(names, ages)
        elif ask == "B":
            review(names, ages)
        elif ask == "Q":
            print("Thank you for participating")
            run = False
        else:
            print("This option does not exist")

menu()
