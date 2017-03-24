import sys
import os
import urllib.request


def main():
    print('Python version {}.{}.{}' . format(*sys.version_info))
    print(sys.platform)
    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd())
    print(os.urandom(25))
    page = urllib.request.urlopen('http://google.com')
    print(page)


if __name__ == '__main__':
    main()

