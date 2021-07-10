
lst = [3,1,5,8,9,4,0]

for i in range(len(lst)):
    for j in range(0, len(lst)-i-1):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1] = lst[j+1], lst[j]
        
print("sorted lst is :", lst)


# Complexity: O(n2)