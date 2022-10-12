# Collect the day
print('Please enter the day: ') #disply instruction
day = int(input()) #collect the input and convert

# Check what day it is
if (day > 0) and (day < 8): #check if it's a valid day
    if day == 1:
        print('Sunday')
    elif day == 2:
        print('Monday')
    elif day == 3:
        print('Tuesday')
    elif day == 4:
        print('Wednesday')
    elif day == 5:
        print('Thursday')
    elif day == 6:
        print('Friday')
    else:
        print('Saturday')
else:
    print('Invalid Format')
