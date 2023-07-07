# How do you remove duplicates from an array in place?

def removeDuplicateNumber(input_list):
    duplicate_nums = []

    input_list = sorted(input_list)
    print("Sorted list - ", input_list)

    for i in range(len(input_list)-1, 0, -1):
        if input_list[i] in input_list[i-1:0:-1]:
            del(input_list[i])

    return input_list
    
input_list = [1,1,2,3,4,6,8,9,10,10,9]
print(removeDuplicateNumber(input_list))