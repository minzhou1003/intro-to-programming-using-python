# minzhou@bu.edu


def sumSeries(i):
    if i == 1:
        return 1/3
    return sumSeries(i - 1) + i / (2.0 * i + 1)


def main():
    for i in range(1, 11):
        print(sumSeries(i))


if __name__ == '__main__':
    main()