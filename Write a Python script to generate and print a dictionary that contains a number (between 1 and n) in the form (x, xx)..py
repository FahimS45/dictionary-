# A Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
def exponent (number):
    dic = {}
    for i in range(number):
        dic[i+1] = (i+1)*(i+1)
    return dic
input_number = int(input("Please enter the number you want to see: "))
print(f'Final output is {exponent(input_number)}')
