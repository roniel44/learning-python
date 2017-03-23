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


def main():
    read_lines()
    read_string()


if __name__ == '__main__':
    main()
