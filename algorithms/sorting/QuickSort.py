# QuickSort with first element as pivot

def swap(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
    return arr

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            swap(arr, i, j)
        else:
            swap(arr, low, j)
    return j

def QuickSort(arr, low, high):
    if low < high:
        j = partition(arr, low, high)
        QuickSort(arr, low, j)
        QuickSort(arr, j+1, high)

def main():
    arr = [5,6,1,4,23,8,0,2]
    QuickSort(arr, 0, len(arr)-1)
    print(arr)

if __name__ == '__main__':
    main()