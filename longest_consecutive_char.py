# Longest Consecutive Characters

def longest(str):
    temp = {}
    count = 0
    for i in str:
        for j in str:
            if i == j:
                count += 1
                temp[i] = count
            else:
                count = 0
    return temp

print(longest('EAABCDDBBBEEEEAE'))