# How do you find the duplicate number on a given integer array?

def findDuplicateNumber(input_list):
    duplicate_nums = []

    for i in range(len(input_list)):
        if input_list[i] in input_list[i+1:]:
            # print(i," ",input_list[i]," ",input_list[i+1:])
            duplicate_nums.append(input_list[i])


    return duplicate_nums
    
input_list = [1,1,2,3,4,6,8,9,10,10,9]
print(findDuplicateNumber(input_list))