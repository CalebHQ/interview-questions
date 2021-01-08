# Find Out Pairs with given sum in an array

def pairs(list, sum):
    list.sort()
    left = 0
    right = len(list) - 1

    while left <= right:
        if list[left] + list[right] > sum:
            right -= 1
        elif list[left] + list[right] < sum:
            left += 1
        elif list[left] + list[right] == sum:
            print(list[left], list[right])
            break



pairs([1, 8, 5, 4, 9, 13, 23, 33], 17)