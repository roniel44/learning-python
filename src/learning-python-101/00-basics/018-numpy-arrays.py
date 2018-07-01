import numpy as np
def main():
    list1 = [1, 2, 3, 5, 6, 7, 8, 9]
    print(list1)

    np_list_1 = np.array(list1)
    print(np_list_1.max())

    print(np_list_1[-1::-2])

    np_list_subset_1 = np_list_1[0:3]

    print(np_list_subset_1)

    np_list_subset_1[:] = 5  # will replace all items in np_list_1 with 5

    print(np_list_1)


if __name__ == '__main__':
    main()
