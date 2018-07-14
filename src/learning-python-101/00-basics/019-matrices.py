def main():
    import numpy as np
    mydata = np.arange(0, 20)
    print(mydata)

    print(np.reshape(mydata, (5, 4)))  # 5 rows, 4 columns
    print(np.reshape(mydata, (2, 10)))  # 2 rows, 10 columns
    print(np.reshape(mydata, (5, 4), order='C'))  # 5 rows, 4 columns, default C-like behaviour
    print(np.reshape(mydata, (5, 4), order='F'))  # 5 rows, 4 columns, default Fortran-like behaviour
    print(mydata.reshape(5, 4))  # call the function from within the object, OOP concept

    matr1 = np.reshape(mydata, (5, 4))
    matr2 = np.reshape(mydata, (5, 4), order='F')

    print(matr1[2, 2])  # get 10
    print(matr2[0, 2])  # get 10

    r1 = ['I', 'am', 'happy']
    r2 = ['What', 'a', 'day']
    r3 = [1, 2, 3]
    npr = np.array([r1, r2, r3])
    print(npr)


if __name__ == '__main__':
    main()
