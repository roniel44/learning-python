import numpy
from numpy.random import randn


def e(x):
    counter = 0

    for u in randn(x):
        if u > -1 and u < 1:
            counter += 1

    return counter/x


def main():
    dists = [10, 100, 1000, 5000]

    for w in dists:
        print('Median distribution for ', w, ' is ', e(w))


if __name__ == '__main__':
    main()
