'''

Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

Insertion Sort Algorithm
To sort an array of size N in ascending order iterate over the array and compare the current element (key) to its predecessor, if the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

'''

dummy_list = [2,1,6,9,3]
print("Original list - ",dummy_list)

for i in range(1,len(dummy_list)):
    key = dummy_list[i] #holds minimum value in sub array

    j = i-1
    while j >= 0 and dummy_list[j]>key :
        dummy_list[j + 1] = dummy_list[j]
        j = j - 1
    dummy_list[j + 1] = key #placing minimum value i.e key at front
    
print("Sorted list - ",dummy_list)