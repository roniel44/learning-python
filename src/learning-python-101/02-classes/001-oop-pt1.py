class Person:
    def get_number_of_legs(self):
        return self.leg_count

    def get_name(self):
        return self.name


class OldLady(Person):
    leg_count = 3
    name = "OldLady"


class Baby(Person):
    leg_count = 4
    name = "Baby"


class Teenager(Person):
    leg_count = 2
    name = "Teenager"


def count_them_legs(people):
    print("A %s has %d legs" % (people.get_name(), people.get_number_of_legs()))


def main():
    old_lady = OldLady()
    baby = Baby()
    teenie = Teenager()

    for person in (old_lady, baby, teenie):
        count_them_legs(person)


if __name__ == "__main__":
    main()
