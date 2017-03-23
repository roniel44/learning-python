def main():
    x, y = 5, 6

    print(id(x))

    print(id(y))

    print(x is y)

    x == y

    print(x is y)

    x = y

    print(x is y)

if __name__ == '__main__':
    main()
