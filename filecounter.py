import os
from fnmatch import fnmatch
import time


def count_files():
    #root = 'C:/Users/2dgam/Desktop/world flags/country flags europe/library/flag'

    root = os.getcwd()
    pattern = "*.png"

    counter = 0

    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                #print os.path.join(path, name)
                counter += 1

    print str(counter) + ' files of type ' + str(pattern) + ' counted.'


if __name__ == "__main__":

    print '___________ FILE COUNTER ___________\n\n'
    start = time.time()
    # call your code here
    count_files()
    end = time.time()
    print('\nFinished in : ' + str(end - start) + 's')

    k = input('Done.\n\nPress any key to close.')