# How do you find the missing number in a given integer array of 1 to 100?

def findMissingNumber(input_list):
    missing_nums = []

    for i in range(1,len(input_list)+1):
        if i not in input_list:
            missing_nums.append(i)
    return missing_nums

input_list = [1,2,3,4,6,8,9,10]
print(findMissingNumber(input_list))