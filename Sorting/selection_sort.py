"""
SELECTION SORT - 
The algorithm repeatedly selects the smallest (or largest) element from the unsorted portion of the list and swaps it with the first element
"""
dummy_list = [2,1,6,9,3]
print("Original list - ",dummy_list)


for i in range(len(dummy_list)):
    min_index = i #index of minimum element

    #Find the minimum element in remaining list
    for j in range(i+1, len(dummy_list)):
        if dummy_list[min_index] > dummy_list[j]:
            min_index = j 
        
    #swap the element with i-th element
    dummy_list[min_index], dummy_list[i] = dummy_list[i], dummy_list[min_index]

print("Sorted list - ",dummy_list)