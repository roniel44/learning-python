def read_lines():

    fh = open("files/lines.txt")

    for line in fh.readlines():
        print(line)


def read_string():

    s = 'some string'

    for i, c in enumerate(s):
        print(i, c)
    else:
        print('iteration done')


def range_test():
    my_list = {1, 2, 3}

    for w in my_list:
        print('item is ', w)

    for p in range(12):
        print('range 12 item number is ', p)


def main():
    read_lines()
    read_string()
    range_test()


if __name__ == '__main__':
    main()
