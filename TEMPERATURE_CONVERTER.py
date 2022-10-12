print('Enter what you want to convert to:\nC for Celcius\nF for Farenheith')
converter = input().lower()
print('Please enter the value:')
value = int(input())

#c = (F-32)*(5/9)

if converter == 'c':
    ans = (value - 32) * (5/9)
    print(f"{value}f is {int(ans)}c")
elif converter == 'f':
    ans = ((9 * value)/5)+32
    print(f"{value}c is {int(ans)}f")
else:
    print('Invalid Format')
