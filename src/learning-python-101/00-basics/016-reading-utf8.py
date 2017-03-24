def main():
    fin = open('files/lines-2.txt', 'r', encoding='utf_8')
    fout = open('files/lines-written.html', 'w')
    outbytes = bytearray()
    for line in fin:
        for c in line:
            if ord(c) > 127:
                outbytes += bytes('%&#{:04d};' . format(ord(c)), encoding='utf_8')
            else:
                outbytes.append(ord(c))
    outstr = str(outbytes, encoding='utf_8')
    print(outstr, file=fout)
    print(outstr)
    print('Donirino')


if __name__ == '__main__':
    main()
