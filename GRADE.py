name = input('Enter your name: ')
score = int(input('Enter your score: '))

if score >= 80:
    print(f"{name} gets A")

elif score >= 60 and score < 70:
    print(f"{name} gets B")
    
elif score >= 55 and score < 60:
    print(f"{name} gets C")

elif score >= 50 and score < 55:
    print(f"{name} gets D")

elif score >= 45 and score < 50:
    print(f"{name} gets E")

else:
    print(f"{name} gets F")
