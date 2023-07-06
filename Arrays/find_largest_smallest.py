# How do you find the largest and smallest number in an unsorted integer array?

def findLargestAndSmallestNumber(input_list):
    largest_num, smallest_num = input_list[0], input_list[0]

    for i in range(1, len(input_list)):
        if input_list[i] > largest_num:
            largest_num = input_list[i]
        
        if input_list[i] < smallest_num:
            smallest_num = input_list[i]
    
    return largest_num, smallest_num

input_list = [2,10,3,4,6,1,8,9,11,10]
print(findLargestAndSmallestNumber(input_list))