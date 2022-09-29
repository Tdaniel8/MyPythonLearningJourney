num1 = input('enter a number: ')
num2 = input ('enter a secound number: ')

if int(num1) > int(num2):
    print(f'{num1} is greater than {num2}')
elif int(num2) > int(num1):
    print(f'{num2} is greater than {num1}')
else:
    print(f'{num1} is equal to {num2}')
