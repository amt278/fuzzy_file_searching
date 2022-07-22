import os

from fuzzywuzzy import fuzz 

root_dir = input('enter the root directory: ')
file_types = input('Enter file types (seperated with space) (empty = all file types): ')
fuzzy_seach = input('Enter file name (empty = all file names): ')

file_types = file_types.split(" ")

found = False

for root, dirs, files in os.walk(root_dir):
    # print(dirs)
    for name in files:
        if name.endswith(tuple(ft for ft in file_types)):# or file_types[0] == "":
            if fuzz.token_sort_ratio(fuzzy_seach.lower(), name.lower()) > 50 or fuzzy_seach == "":
                found = True
                print(root + os.sep + name)

if not found:
    print('there is no files matching the pattern')