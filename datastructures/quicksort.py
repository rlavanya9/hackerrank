def quicksort(arr):
    if len(arr) < 2:
        return arr
    
    elements = len(arr)
    current_pos = 0
    for i in range(1,elements):
        if arr[i] < arr[0]:
            current_pos += 1
            arr[i], arr[current_pos] = arr[current_pos], arr[i]
    
    arr[0], arr[current_pos] = arr[current_pos], arr[0]

    left = quicksort(arr[0:current_pos])
    right = quicksort(arr[current_pos+1:elements])

    srt_arr = left + [arr[current_pos]] + right

    return srt_arr

array_to_be_sorted = [4,2,7,3,1,6]
print("Original Array: ",array_to_be_sorted)
print("Sorted Array: ",quicksort(array_to_be_sorted))