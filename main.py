# Write a Python program to find the key of the maximum value in a dictionary. Go to the editor
given = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
def max_min_key(dict):
    from operator import itemgetter
    new_dict = sorted(dict.items(), key = itemgetter(1))
    length = len(dict)
    max = new_dict[length-1][1]
    min = new_dict[0][1]
    return  max, min
result = max_min_key(given)
print("Maximum is %i and Minimum is %i"%result)