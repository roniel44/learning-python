class Bird:
    def tweet(self):
        print("tweet")


class Dog:

    def bark(self):
        print("worf")


def make_dog_bark(dog):
    dog.bark()


def make_bird_tweet(bird):
    bird.tweet()


def main():
    dodo = Bird()
    fido = Dog()
    make_bird_tweet(dodo)
    make_dog_bark(fido)

if __name__ == '__main__':
    main()
