s1 = {10: 'one', 2: 'two', 3: 'three', 1: {100: 'ten', 20: 'twenty'}}
print(type(s1))
s2 = s1.copy()
s2[10] = 'ten'
s1[1][100] = 'one'
print(s1)
print(s2)
