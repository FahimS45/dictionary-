# A Python program to filter the height and width of students, which are stored in a dictionary.
d1 = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66), 'Michael Scott': (6.3,71)}

def hw_filter (height,weight):
    for each in d1:
        tup = d1[each]
        if tup[0]<=height and tup[1]<=weight:
            print(f"{each} : {tup[0]}ft and {tup[1]}kg")
        continue

for name in d1:
    tup_name = d1[name]
    print(f"{name} : \t\t\t\t {tup_name[0]}ft {tup_name[1]}kg")
input_height = float(input("Please enter the height: "))
input_weight = float(input("Please enter the weight: "))
hw_filter(input_height,input_weight)