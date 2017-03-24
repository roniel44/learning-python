class Chair:

    def __init__(self, **kwargs):
        self._properties = kwargs

    def set_property(self, key, value):
        self._properties[key] = value

    def get_property(self, key):
        return self._properties[key]

    @property
    def color(self):
        return self._properties.get('color', None)

    @color.setter
    def color(self, c):
        self._properties['color'] = c

    @color.deleter
    def color(self):
        del self._properties['color']


def main():
    my_chair = Chair()
    my_chair.color = 'green'
    print(my_chair.color)


if __name__ == '__main__':
    main()
