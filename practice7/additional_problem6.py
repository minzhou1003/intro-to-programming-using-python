# minzhou@bu.edu


def complementary(x, y):

    dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    tmp = []
    for i in x:
        tmp.append(dict[i])
    tmp_str = ''.join(str(e) for e in tmp)
    if tmp_str == y[::-1]:
        return True
    else:
        return False


def main():
    s = input('Enter two DNA sequence seperated by space: ').split()
    x = s[0]
    y = s[1]
    if complementary(x, y):
        print('{} and {} are complementary'.format(x, y))
    else:
        print('{} and {} are NOT complementary'.format(x, y))


main()