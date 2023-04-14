# a Python program to combine two dictionary by adding values for common keys.
def comkeys (dic1, dic2):
    from operator import itemgetter
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
    # sorting in ascending order
    d_new_sorted = dict(sorted(d_new.items(), key = itemgetter(0)))
    return d_new_sorted

# let's say two dictionaries are:
d1 = {'a': 100, 'b': 200, 'c': 300, 'f': 700, 'g': 1000}
d2 = {'a': 300, 'b': 200, 'd': 400, 'g': 100, 'e': 600}
result = comkeys (d1,d2)
print(f"Finsl output is {result}")


