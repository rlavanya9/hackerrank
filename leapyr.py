def is_leap(year):
    leap = False
    #A leap year is exactly divisible by 4 except for century years (years ending with 00). The century year is a leap year only if it is perfectly divisible by 400. For example,
    # Write your logic here
    if(year%4 == 0): 
        if(year%100 == 0):
            if(year%400 == 0):
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
         leap = False   
                
    return leap

print(is_leap(1992))