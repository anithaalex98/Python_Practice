'''
Bubble sort - 
In this algorithm, 

traverse from left and compare adjacent elements and the higher one is placed at right side. 
In this way, the largest element is moved to the rightmost end at first. 
This process is then continued to find the second largest and place it and so on until the data is sorted.

'''

dummy_list = [2,1,6,9,3]
print("Original list - ",dummy_list)

for i in range(len(dummy_list)):
    for j in range(0,len(dummy_list)-i-1): #for i=0, j is range(0,4) that is j=0 to j=3
        if dummy_list[j]>dummy_list[j+1]: #compares which element is greater then swaps
            dummy_list[j], dummy_list[j+1] = dummy_list[j+1], dummy_list[j]
print("Sorted list - ",dummy_list)