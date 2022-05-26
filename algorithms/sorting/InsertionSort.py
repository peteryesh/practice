from common import swap

def InsertionSort(arr):
    for i, item in enumerate(arr):
        j = i
        while j > 0 and item < arr[j-1]:
            print(item, arr[j-1])
            swap(arr, j, j-1)
            j -= 1


def main():
    arr = [2, 8, 5, 3, 9, 4]
    InsertionSort(arr)
    print(arr)

if __name__ == '__main__':
    main()