def my_generator(n):
    yield n
    yield n + 1


def main():
    for n in my_generator(6):
        print(n)

if __name__ == '__main__':
    main()
