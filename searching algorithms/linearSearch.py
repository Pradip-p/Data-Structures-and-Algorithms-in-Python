# Linear search is a sequential searching algorithm where we start from one end and check every element of the list until the desired element is found. 
# It is the simplest searching algorithm.


def linear_search(lst,n):

    # Going through array sequencially
    for index in range(0, len(lst)):

        if (lst[index] == n):
            return index
    return False

    
            
lst = [100,101,200,201,300,3001]
n = 300
result = linear_search(lst, n)
if result == False:
    print("Element not Found")
else:
    print("Element is found at index:", result)