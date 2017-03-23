class Person:
    def getNumberOfLegs(self):
        return self.legCount;

    def getName(self):
        return self.name;


class OldLady(Person):
    legCount = 3;
    name = "OldLady";


class Baby(Person):
    legCount = 4;
    name = "Baby";


class Teenager(Person):
    legCount = 2;
    name = "Teenager";


def count_them_legs(people):
    print("A %s has %d legs" % (people.getName(), people.getNumberOfLegs()));


def main():
    oldLady = OldLady();
    baby = Baby();
    teenie = Teenager();

    for person in (oldLady, baby, teenie):
        count_them_legs(person);


if __name__ == "__main__":
    main();
