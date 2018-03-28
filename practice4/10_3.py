# minzhou@bu.edu

def get_occur():
    numbers = list(map(int, input('Enter integers between 1 and 100: ').split()))
    dict = {}
    for number in numbers:
        if number in dict:
            dict[number] += 1
        else:
            dict[number] = 1
    for key in dict:
        if dict[key] > 1:
            print('{} occurs {} times'.format(key, dict[key]))
        else:
            print('{} occurs 1 time'.format(key))

get_occur()