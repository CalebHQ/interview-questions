# FIND MISSING NUMBER IN AN ARRAY

def missing(list):
    last_num = list[-1]
    natural_sum = (last_num * (last_num + 1)) // 2
    
    sum = 0
    for i in list:
        sum += i

    missing_number = natural_sum - sum
    return missing_number


print(missing([1, 2, 3, 4, 6, 7, 8, 9, 10]))
