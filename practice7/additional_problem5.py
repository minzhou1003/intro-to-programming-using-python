# minzhou@bu.edu


def sort_in_place(arr):

    n = len(arr)

    for i in range(n):

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]



def move_left(arr):

    n = len(arr)
    i = -1
    for j in range(n):

        if (arr[j] > 0):
            i += 1
            # swapping of arr
            arr[i], arr[j] = arr[j], arr[i]



def main():

    arr = [2, 6, -6, -3, 1, 19]
    print('Original array is:', arr)
    
    sort_in_place(arr)
    move_left(arr)

    print('Sorted array is:', arr)

main()