def main():
    num1 = 100
    num2 = 15
    sum1 = num1 + num2
    floor_division = num1 // num2;

    # simple displaying of sum
    print("num1 + num2 = ", sum1)

    # multiplication on the go using format string
    print("multiple %d by %d and you get %d" % (num1, num2, (num1 * num2)))
    my_position = 69

    my_like = "kpop"

    my_name = "Lion Heart"
    my_age = 35

    print("my favorite position is %d" % my_position)
    print("i like %s" % my_like)

    # combination of string + number
    print("im %s and im %d years old" % (my_name, my_age))

    print("flour quotient is %d " % floor_division)

    some_float = 5.555123

    print(some_float)


if __name__ == '__main__':
    main()
