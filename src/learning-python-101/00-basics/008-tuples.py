def main():
    # tuples are read only lists
    tuple = ("abcd", 123, "john", "dignity", 3.14, "000000")
    tiny_tuple = ("road", "rage")
    print(tuple)
    print(tuple + tiny_tuple)

    # this throws an error i think
    # tuple[0] = "something"

    # most of these you can google google
    print(len(tuple))  # length

    is_exist = 123 in tuple  # should be true
    print(is_exist)


if __name__ == '__main__':
    main()
