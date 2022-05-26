def merge(arr1: list, arr2: list):
    i = 0
    j = 0
    merged = []
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            merged.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            merged.append(arr1[i])
            i += 1
        elif arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    return merged

def mergeSort(arr: list):
    if len(arr) <= 1:
        return arr
    mid = int(len(arr)/2)
    arr1 = mergeSort(arr[0:mid])
    arr2 = mergeSort(arr[mid:len(arr)])
    print(arr1, arr2)
    return merge(arr1, arr2)

def main():
    print(mergeSort([1,2,3,4,5,6,7]))
    print(mergeSort([7,6,5,4,3,2,1]))
    print(mergeSort([1,3,7,2,5]))
    print(mergeSort([]))
    print(mergeSort([1,2]))
    print(mergeSort([2,1]))
    print(mergeSort([13,1,2,3,4,12,7,9,2,3]))

if __name__ == '__main__':
    main()