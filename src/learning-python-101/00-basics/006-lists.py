def main():
    listerino = ["abcd", 123, "john", "dignity", 3.14, "000000"]
    le_small_list = ["jack", "rose"]
    print(list)
    # indexing works like in php
    print(listerino[0])  # prints abcd
    print(listerino[3:])  # prints from index onwards
    print(listerino[0:2])  # prints from index 0,  2 items
    print(le_small_list * 2)  # prints small list twice
    print(le_small_list + listerino)  # prints small list + the list

    listerino[0] = "abcde"  # replace item in list
    print(listerino)
    print(listerino[-1]) #prints last item in list
    print(listerino[-5:-1]) # example of negative index slicing

    numbers_list = [5, 3, 4, 1, 2]
    # sorting, this is googable
    # only works on all string/numbers list
    print(numbers_list)
    numbers_list.sort()
    print(numbers_list)
    # min works as well
    print(max(numbers_list))

    lists_multidimention = [numbers_list, le_small_list]

    print(lists_multidimention)

    # does nothing
    z1 = range(1, 2)

    # creates list
    z2 = list(range(1, 15))

    # specify multiples of 3rd parameter
    z3 = list(range(0, 150, 5))

    print(z1)
    print(z2)
    print(z3)


    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    print(alphabet[2:7])  #element 3 to element before 7 (6)
    print(alphabet[-8:7]) #another example of negative slicing
    print(alphabet[2::2]) #specify a step, without specifying ending elents
    print(alphabet[-10:-1:2]) #step with negative indices

if __name__ == '__main__':
    main()
