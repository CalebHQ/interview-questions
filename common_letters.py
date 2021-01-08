# Find out common letters between two strings

def common_letters(str1, str2):
    common = []
    for i in str1:
        for j in str2:
            if i == j:
                if i not in common:
                    common.append(i)
    return common

print(common_letters('NAINA', 'REENE'))
