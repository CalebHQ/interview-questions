# Conversion of two list into Dictionary

def convert(list1, list2):
    temp = {}
    list2_index = 0
    for i in list1:
        temp[i] = list2[list2_index]
        list2_index += 1
    return temp


print(convert(['John', 'Caleb', 'Alex'], [2134, 3422, 4532]))