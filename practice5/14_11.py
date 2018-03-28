# minzhou@bu.edu

import os.path
import collections
import sys

def main():

    vowels = set('AEIOU')

    filename = input("Enter a Python source code filename: ").strip()

    if not os.path.isfile(filename): # Check if file exists
        print("File", filename, "does not exist")
        sys.exit()

    
    infile = open(filename, "r") # Open files for input

    text = infile.read().split() # Read and split words from the file 21

    cnt_vowels = 0
    cnt_consonants = 0
    for word in text:
        for letter in word:
            if letter.upper() in vowels:
                cnt_vowels += 1
            else:
                cnt_consonants += 1
            
    print('There are {} vowels and {} consonants in the file'.format(cnt_vowels, cnt_consonants))


main()
                