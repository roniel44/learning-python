def main():
    my_string = 'My String'
    split_string = my_string.split()
    rejoined_string = ':' . join((split_string))
    print(my_string.upper())
    print(my_string.lower())
    print(my_string.swapcase())
    print(my_string.find('My'))
    print(id(my_string))
    print(my_string.strip('M'))
    print(my_string.strip('g'))
    print(my_string.isalnum())
    print(my_string.split('y'))
    print(rejoined_string)
    print(split_string)


if __name__ == '__main__':
    main()
