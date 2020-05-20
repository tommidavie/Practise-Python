# loops

# loops are repeated

# a loop with a counter (will run a certain number of times)

def loop_with_counter():
    c = 0
    while c < 10:
        print("hello c is now {}".format(c) )
        # increment c
        c += 1
    return None

# indefinate loop

def indefinite_loop():
    run = True
    while run == True:
        user_choice = input("Press 'n' to stop the loop or anything else to stay in it -> ")
        if user_choice == "n":
            print("Loop will stop")
            run = False
        else:
            print("You are still in the loop")

# loop_with_counter()

# indefinate_loop()

def for_in_range_loop():
    
    # this has a bulit in counter
    # can be anything but we generally use i or j or k
    # can add steps (integer)
    # first number, after last number, increment number (steps)
    # if you put no step, then it's one\
    
    for i in range(3, 20, 5):
        print(i)

# double loop

def double_loop():
    for i in range(0,5):
        for j in range(0,6):
            print( "({},{})".format(j,i) , end = "" )
        print()

# double_loop()

def menu():
    run = True
    while run == True:
        
        my_menu = '''
        1: while loop with counter
        2: while loop with quit
        3: for in range
        4: double loop
        0: quit
        '''
        print (my_menu)
        choice = int(input("choose your option: -> "))
        if choice == 1:
            amount = int(input("How many would you like: -> "))
            loop_with_counter()
        elif choice ==2:
            indefinite_loop()
        elif choice == 3:
            for_in_range_loop()
        elif choice == 4:
            double_loop()
        elif choice == 0:
            run = False
            print("Thanks for playing")
        else:
            print("Unrecognised entry")
menu()










