def swap(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
    return arr

def heapify(arr):
    i = len(arr)-1
    while i >= 0:
        trickleHeap(arr, i, len(arr)-1)
        i -= 1

def trickleHeap(arr, i, end):
    left = 2*(i+1)-1
    right = 2*(i+1)
    while i < end:
        if left < end and right < end:
            if arr[left] > arr[right] and arr[left] > arr[i]:
                swap(arr, i, left)
                i = left
            elif arr[right] > arr[left] and arr[right] > arr[i]:
                swap(arr, i, right)
                i = right
            else:
                return
        elif left < end and right >= end and arr[left] > arr[i]:
            swap(arr, i, left)
            i = left
        else:
            return
        left = 2*(i+1)-1
        right = 2*(i+1)

def HeapSort(arr):
    heapify(arr)
    i = len(arr) - 1
    while i >= 0:
        swap(arr, 0, i)
        print(arr)
        trickleHeap(arr, 0, i)
        i -= 1
        

def main():
    arr = [10, 20, 15, 12, 40, 25, 18]
    HeapSort(arr)
    print(arr)

if __name__ == '__main__':
    main()