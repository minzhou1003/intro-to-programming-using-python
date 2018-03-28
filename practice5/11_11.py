# minzhou@bu.edu


def decimal2binary(number):

    binary_seq = []

    while number:
        binary_seq.append(number % 2)
        number = number // 2
    while len(binary_seq) < 9:
        binary_seq.append(0)
    return binary_seq[::-1]


def print_res(binary_seq):

    for i in range(9):
        if binary_seq[i] == 0:
            binary_seq[i] = 'H'
        else:
            binary_seq[i] = 'T'
    
    for j in [0, 3, 6]:
        res = ' '.join(binary_seq[j:j+3])
        print(res)


def main():
    number = int(input('Enter a number between 0 and 511: '))
    print_res(decimal2binary(number))


main()
