def binar_search_arr(a, key, low, high):
    if low > high:
        return -1
    
    mid = low + ((high-low)//2)
    if a[mid] == key:
        return mid
    elif key > a[mid]:
        return binar_search_arr(a, key, mid + 1, high)
    else:
        return binar_search_arr(a, key, low, mid-1)

def binary_search(a, key):
    return binar_search_arr(a, key, 0, len(a)-1)