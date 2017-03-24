def main():
    buffer_size = 50000
    readfile = open('files/many-lines.txt', 'r')
    writefile = open('files/new.txt', 'w')
    buffer = readfile.read(buffer_size)

    while len(buffer):
        writefile.write(buffer)
        buffer = readfile.read(buffer_size)

    print('Done')


if __name__ == '__main__':
    main()
