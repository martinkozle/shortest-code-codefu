from os import listdir
from time import sleep

from length_calculator import get_len


def main():
    folder = './12/'
    files = listdir(folder)
    files = list(filter(lambda x: x.endswith('.py'), files))
    print(files)
    while True:
        print('\r', end='')
        for file_name in files:
            length = get_len(folder + file_name)
            print(f'{file_name}: {length}    ', end='')
        sleep(1)


if __name__ == '__main__':
    main()
