class Egg:
    def __init__(self):
        self._kind = "fried"

    def set_kind(self, kind):
        self._kind = kind

    def get_kind(self):
        return self._kind


def main():
    fried = Egg()
    scrambled = Egg()
    scrambled.set_kind("scrambled")
    print(fried.get_kind())
    print(scrambled.get_kind())


if __name__ == '__main__':
    main()
