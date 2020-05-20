def adding(a,b):
    my_sum = a+b
    # make a string
    my_string = "{} + {} = {}".format(a,b,my_sum)
    print (my_string)

#adding(2,8)

def subtracting(a,b):
    my_sum = a-b
    my_string = "{} - {} = {}".format(a,b,my_sum)
    print (my_sum)

#subtracting(9,5)

def multiplying(a,b):
    my_sum = a*b
    my_string = "{} * {} = {}".format(a,b,my_sum)
    print (my_sum)

#multiplying(5,5)

def dividing(a,b):
    my_sum = a/b
    my_string = "{} / {} = {}".format(a,b,my_sum)
    print (my_sum)

#dividing(81,9)

def get_integer(m):
    my_number = int(input("Please enter your number: -> "))
    return my_number

m = menu
    
def menu():

    num_one = get_integer("Please enter your first number: ")
    num_two = get_integer("Please enter your second number: ")
    
    my_menu = '''
    1 : add
    2 : subtract
    3 : multiply
    4 : divide
    0 : quite
    '''

    
    print(my_menu)

    choice = get_integer (m)

    if choice == 1:
        adding(num_one, num_two)

    elif choice == 2:
        subtracting(num_one, num_two)

    elif choice == 3:
        multiplying(num_one, num_two)

    elif choice == 4:
        dividing(num_one, num_two)

    else:
        print("This was not an option")
    
menu()

get_integer("My message")

