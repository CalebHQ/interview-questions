# Count the frequency of words appearing in a string

def count_freq(str):
    temp = {}
    list = str.split(' ')
    for item in list:
        if item not in temp:
            temp[item] = 1
        else:
            temp[item] += 1
    return temp

print(count_freq('Caleb loves to eat apples but always loves to eat bananas'))