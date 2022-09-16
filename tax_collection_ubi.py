import numpy as np
import random

# print(data[0])

def generate_dic_values(num, size, mul):
    data = np.random.dirichlet(np.ones(num),size=size)
    # print(data)
    dictvalues = {}
    y = 0
    for x in data[0]:
        dictvalues[y] = x*mul
        y = y + 1
    return dictvalues



#Tax 4 random values
def generate_radom_numbers(rg, num):
    randomlist = []
    for i in range(0,rg):
        n = random.randint(0,num)
        randomlist.append(n)
        
    return randomlist

# Collect 5% tax 
def tax_collection(dictvalues, randomlist):
    total_tax = 0
    for li in randomlist:
        value = dictvalues[li]
        tax = (value * 5)/100
        total_tax = tax + total_tax
        left_value = value - tax
        dictvalues[li] = left_value
    return (total_tax, dictvalues)

# Distribute tax equally to peoples
def distribute_tax(total_tax, num, dictvalues):
    individual_income = total_tax/num
    for x in range(0, num):
        value = dictvalues[x]
        add_value = value + individual_income
        dictvalues[x] = add_value
    return dictvalues





 
if __name__ == "__main__":
    num = 10
    dictvalues = generate_dic_values(num, 1, 1000)
    print(dictvalues)
    
    for x in range(1000):
        randomlist = generate_radom_numbers(4, num-1)       
        (total_tax, dictvalues) = tax_collection(dictvalues, randomlist)
        # print(randomlist)
        # print(total_tax)
        dictvalues = distribute_tax(total_tax, num, dictvalues)

    # New values are more equal, reducing income inequality
    print(dictvalues)

# Example values
# Intial
# {0: 145.73066800489423, 1: 43.00866767658919, 2: 283.46082318329866, 3: 123.31971833921949, 4: 143.80255958101523, 5: 7.634156152591173, 6: 62.95130099146863, 7: 65.21259591708083, 8: 8.11855160833787, 9: 116.76095854550476}
# Final
# {0: 96.00241898297, 1: 104.36193050518715, 2: 88.54176705013242, 3: 86.5786303910261, 4: 98.26584136732163, 5: 114.61915251476192, 6: 104.62382043478628, 7: 121.90985100585453, 8: 94.15798957991514, 9: 90.93859816804566}

