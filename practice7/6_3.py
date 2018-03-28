# minzhou@bu.edu


# Return the reversal of an integer, e.g. reverse(456) returns # 654
def reverse(number):

    return str(number)[::-1]


# Return true if number is a palindrome
def isPalindrome(number):

    if reverse(number) == str(number):
        return True
    else:
        return False


def main():

    number = int(input('Enter an integer: '))
    if isPalindrome(number):
        print('The integer is a palindrome')
    else:
        print('The integer is NOT a palindrome')

main()