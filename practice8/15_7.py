# minzhou@bu.edu


count = 0


def fib(index):

    global count
    count +=1
    if index == 0:  # Base case
        return 0
    elif index == 1:  # Base case
        return 1
    else:  # Reduction and recursive calls
        return fib(index - 1) + fib(index - 2)


def main():

    index = eval(input("Enter an index for a Fibonacci number: "))
    # Find and display the Fibonacci number
    print("The Fibonacci number at index", index, "is", fib(index))

    print("The fib method was called " + str(count) + " times")


if __name__ == '__main__':
    main()