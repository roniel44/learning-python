def main():
    my_string = 'My String'
    print(my_string.upper())
    print(my_string.lower())
    print(my_string.swapcase())
    print(my_string.find('My'))
    print(id(my_string))
    print(my_string.strip('M'))
    print(my_string.strip('g'))
    print(my_string.isalnum())


if __name__ == '__main__':
    main()
