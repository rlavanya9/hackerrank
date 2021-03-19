# def binary_search_arr(a, key, low, high):

#     if low > high:
#         return -1
    
#     mid = low + ((high-low)//2)

#     if a[mid] == key:
#         return mid
#     elif key < a[mid]:
#         return binary_search_arr(a, key, low, mid-1)
#     else:
#         return binary_search_arr(a, key, mid+1, high)
    
# def binary_search(a, key):
#     return binary_search_arr(a, key, 0, len(a)-1)

# arr = [1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162, 176, 188, 199, 200, 210, 222]
# inputs = [10, 49, 99, 110, 176]

# for i in range(len(inputs)):
#   print("binary_search(arr, " + str(inputs[i])+ ") = " +  str(binary_search(arr, inputs[i])))


# inventory = [15, 100, 110, 200]
# you want to return output that has atleast 105

# input:
# capacity needed, list of inventory

# output:
# closest match for inventory

def Inventory_Match(capacity, myinvent, low, high):
    match = []
    
    mid = low + ((high-low)//2)

    if myinvent[mid] == capacity:
        return myinvent[mid]
    elif myinvent[mid] > capacity:
        return Inventory_Match(capacity,myinvent, low, mid-1)
    else:
        return Inventory_Match(capacity, myinvent, mid+1, high)

def Invent(capacity, myinvent):
    return Inventory_Match(capacity, myinvent, 0, len(myinvent)-1)
    

    # for element in myinvent:
    #     if element >= capacity:
    #         match.append(element)
    #         print(match)
    # match_srt = sorted(match)
    # return match_srt[0]

print(Inventory_Match(105,[15,100,110,200]))




