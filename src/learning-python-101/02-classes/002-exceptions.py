try:
    fh = open("something")
    for line in fh.readlines():
        print(line)
except IOError as e:
    print("lmao file does not exisit i think ({})".format(e))


print("post exception stuff")