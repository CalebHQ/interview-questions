# First Recurring Character

def first_recurring_char(str):
    for i in str:
        if str.count(i) >= 2:
            return i
    return None
    
print(first_recurring_char('ABCA'))

def first_recurring_char_dict(str):
    temp = {}
    for s in str:
        if s not in temp:
            temp[s] = 1
        else:
            temp[s] += 1
            return s
    return None

print(first_recurring_char_dict('ABCA'))