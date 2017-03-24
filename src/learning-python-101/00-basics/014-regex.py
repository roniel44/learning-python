import re


def main():
    fh = open('files/the-cross-lyrics.txt')
    pattern = '(wait|li)ed'
    for line in fh:
        if re.search(pattern, line):
            print(line)

    fh2 = open('files/the-cross-lyrics.txt')
    for line2 in fh2:
        match = re.search(pattern, line2)
        if match:
            print(match.group())

    fh3 = open('files/the-cross-lyrics.txt')
    for line3 in fh3:
        match = re.search(pattern, line3)
        if match:
            print(re.sub(pattern, 'replaced', line3))


if __name__ == '__main__':
    main()
