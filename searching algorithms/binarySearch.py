# Binary search can be implemented only on a sorted list of items. If the elements are not sorted already, we need to sort them first.


def binary_search(lst, n, low, high):
    
    # Repeat until the pointers low and high meet each other
    while low <= high:
        mid = low + (high - low) // 2
    
        if lst[mid] == n:
            return mid
        
        elif lst[mid] < n:
            low = low + 1
        else:
            high = high - 1
    return -1

lst = [1,3,2,5,6,7,9,10,0,11]
lst.sort()
n = 10
low = 0
high = len(lst) - 1
result = binary_search(lst, n,low, high)
if result != -1:
    print("Element is found at index", result)
else:
    print("Element is not found")
    