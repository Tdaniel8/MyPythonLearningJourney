print('Please enter the day:')
day = int(input())

days_of_week = ['Sunday','Monday','Tuesday','Wednesday',
                'Thursday','Friday','Saturday']

if (day > 0) and (day < 8):
    print(days_of_week[day-1])
else:
    print('Invalid Format')
