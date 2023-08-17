def insert_sort(arr):
    for i in range(1, len(arr)):
        # key to store the value to compare with other elements
        key = arr[i]
        # j to point current comparing element(with the key) in the array
        j = i-1
        # k to move comparing pairs (since i cannot be moved )
        k = i
        while j >= 0 and key < arr[j]:
            arr[k] = arr[j]
            j -= 1
            k -= 1
        arr[k] = key
        print(arr)
    return arr


arr1 = [10, 3, 6, 2, 1]
print(arr1)
print(insert_sort(arr1))
