def dub_loop_print(L):
    for i in range(0, len(L)):
        output = "{} :{}".format(i, L[i])
        print(output)
        for j in range(0,len(L[i])):
            output = "{} : {}".format(j, L[i][j])
            print(output)

dub_loop_print()

def main():
    my_list=[
             ["Nia", "Blond", "16"],
             ["Tommi", "Blond","16"],
             ["Grace", "Brown", "16"],
             ["Rebecca", "Black", "16"],
             ["Grace", "Brown", "16"]
             ]
    #print(my_list)

    for i in range(0, len(my_list)):
        out = "{:<10} -- {:<10} -- {:<10}".format(my_list[i][0], my_list[i])

main()