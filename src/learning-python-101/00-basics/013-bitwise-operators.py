def main():

    # 60 = 0011 1100
    a = 60

    # 13 = 0000 1101
    b = 13

    c = 0

    # 12 = 0000 1100
    c = a & b
    print("Line 1 - Value of c is ", c)

    # 61 = 0011 1101
    c = a | b
    print("Line 2 - Value of c is ", c)

    # 49 = 0011 0001
    c = a ^ b
    print("Line 3 - Value of c is ", c)

    # -61 = 1100 0011
    c = ~a
    print("Line 4 - Value of c is ", c)

    # 240 = 1111 0000
    c = a << 2
    print("Line 5 - Value of c is ", c)

    # 15 = 0000 1111
    c = a >> 2
    print("Line 6 - Value of c is ", c)


if __name__ == '__main__':
    main()
