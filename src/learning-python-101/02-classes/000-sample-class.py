class Car:
    def __init__(self, type, color):
        print("constructor called")
        self.type = type
        self.color = color

    def describe(self):
        print("I have a %s, color is %s" % (self.type, self.color))


def main():
    car1 = Car("Hyundai", "Green")
    car1.describe()


if __name__ == '__main__':
    main()
