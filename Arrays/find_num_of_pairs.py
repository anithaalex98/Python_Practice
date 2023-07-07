# How do you find all pairs of an integer array whose sum is equal to a given number? 

def findListOfSum(input_list,sum):
    no_of_pairs = 0

    for i in range(len(input_list)):
        for j in range(i+1, len(input_list)):
            if input_list[i] + input_list[j] == sum:
                print("Pairs - ",input_list[i], ",",input_list[j])
                no_of_pairs += 1

    return no_of_pairs
    
input_list = [1, 5, 7, -1]
sum = 6
print(findListOfSum(input_list,sum))