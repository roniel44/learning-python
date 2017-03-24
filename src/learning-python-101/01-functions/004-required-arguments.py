# basic required arguments
# This prints a passed string into this function


def ask_name(name):
    print("you think %s is the GOAT" % name)
    return


def main():
    rapper = input("who's the best rapper eva? ")
    ask_name(rapper)


if __name__ == '__main__':
    main()


