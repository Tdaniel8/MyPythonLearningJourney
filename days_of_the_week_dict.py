print('Please enter the day:')
day = int(input())

days_of_week = {1:'Sunday',2:'Monday',3:'Tuesday',4:'Wednesday',5:'Thursday',6:'Friday',7:'Saturday'}


if (day > 0) and (day < 8):
    print(days_of_week[day-0])
else:
    print('Invalid Format')
     
