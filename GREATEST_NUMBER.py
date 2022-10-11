num1 = input('enter a number: ')
num2 = input ('enter a secound number: ')
num3 = input ('enter a third number: ')

if int(num1) > int(num2) and  int(num1) > int(num3):
    print(f'{num1} is the greatest')
elif int(num2) > int(num3) and int(num2) > int(num1):
    print(f'{num2} is the greatest')
else:
    print(f'{num3} is the greatest')
    
