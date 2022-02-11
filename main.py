import math
def geometricSeriesSum(firstTerm,numbers,ratio):
    sum = 0
    if(ratio == 1):
        print("invalid input") 
    else:
        sum = (firstTerm * (1- math.pow(ratio,numbers)))/(1-ratio)
    print("sum is: ", sum) 

def findNthTermGeometric(firstTerm,ratio,n):
    nthTerm = firstTerm * (math.pow(ratio,n-1))
    print("nth term is: ", nthTerm)

print("What you want you find of a GP: ")
print("\t 1. For finding GP Series sum enter '1'")
print("\t 2. For finding nth Term of the GP enter '2' ")

WhatToDo = raw_input()

WhatToDo = int(WhatToDo)

if(WhatToDo == 1):
    FTerm = int(raw_input("enter the first term of the GP: "))
    num = int(raw_input("Enter the number of terms you want in the series: "))
    rat = int(raw_input("Enter the Common ratio: "))
    geometricSeriesSum(FTerm,num,rat)
elif(WhatToDo == 2):
    FTerm = int(raw_input("enter the first term of the GP: "))
    num = int(raw_input("Enter the number of terms you want in the series: "))
    rat = int(raw_input("Enter the Common ratio: "))
    findNthTermGeometric(FTerm,rat,num)
else:
    print ("invalid input")
    
