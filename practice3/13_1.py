# copyright minzhou@bu.edu

def remove():
    # input file should be in the same folder as the .py file
    # input file 'test.txt'
    filename = input('Enter a filename: ')
    f = open(filename, 'r')
    # save the result to 'result_file.txt'
    res = open('result_file.txt', 'w')
    # remove 'programming'
    word = input('Enter the string to be removed: ')
    res.write(f.read().replace(word, ''))   
    f.close
    res.close
    print('Done')

remove()