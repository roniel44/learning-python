class Chair:

    def __init__(self, **kwargs):
        self._properties = kwargs

    def set_property(self, key, value):
        self._properties[key] = value

    def get_property(self, key):
        return self._properties[key]


def main():
    my_chair = Chair()
    my_chair.set_property("color", "green")
    print(my_chair.get_property("color"))


if __name__ == '__main__':
    main()
