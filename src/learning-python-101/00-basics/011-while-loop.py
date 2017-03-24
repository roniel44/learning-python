# simple fibonacci using while loop

def main():
    a, b = 0, 1

    while b < 50:
        print(b)
        a, b = b, a + b
    print("Done")


if __name__ == '__main__':
    main()

