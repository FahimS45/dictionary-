d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d_new = {}
sum = 0
for each_key1 in d1.keys():
    for each_key2 in d2.keys():
        if each_key1 == each_key2:
            sum = d1[each_key1] + d2[each_key2]
            d_new[each_key1] = sum
            sum = 0
        elif each_key2 not in d1.keys():
            d_new[each_key2] = d2[each_key2]
        elif each_key1 not in d2.keys():
            d_new[each_key1] = d1[each_key1]
print(d_new)
