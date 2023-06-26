#reversing a list using slicing within the list
dummy_list = [1,2,6,9,3]
print("Original list - ",dummy_list)
dummy_list = dummy_list[::-1]
print("Reversed list - ",dummy_list)

#reversing a list using for loop within the list
dummy_list2 = [1,2,6,9,3]
print("Original list - ",dummy_list2)
temp = 0
for i in range((len(dummy_list2)//2)+1): #iterates from i=0 to i=3
    temp = dummy_list2[i]
    dummy_list2[i] = dummy_list2[-(i+1)]
    dummy_list2[-(i+1)] = temp
print("Reversed list - ",dummy_list2)

#reversing a list using in-built function, within the list
dummy_list3 = [1,2,6,9,3]
print("Original list - ",dummy_list3)
dummy_list3.reverse()
print("Reversed list - ",dummy_list3)