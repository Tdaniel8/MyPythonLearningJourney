str1 = 'this is a string in python' #sibgle quote string
print(str1)
str2 = "this is a string in python" #double quote string
print (str2)

str3 = '''this is my
first multi-line
string''' #triple single quote string
print (str3)
str4 = """this is
    my secound
multi-line string """ #tripple double quote string
print(str4)

str5 = 'welcome to "Engineer-D python tutorial"' #using double quote inside single quote
print(str5)
str6 = "welcome to 'Engineer-T pythong tutorial'" #using single quote inside double quote
print(str6)

str7 = "Olusola tosin daniel"
print(len(str7)) #printing out the length of str7
str8 = 'Olashinde oyindamola'
print(len(str8)) #printing out the length of str8

str9 = 'Engineer-D'
print(len(str9))

print(str9[0]) #printout the first index
print(str9[9]) #printout the last index
print(str9[-10]) #printout the first index using negative method
print(str9[-1]) #printout the last index using negative method

print(str9[2]) #printout the 3rd index
print(str9[7]) #printout the 8th index
print(str9[-8]) #printout the 3rd index using the negative method
print(str9[-3]) #printout the 8th index using the negative method

print(str(100)) #converting Int 100 to string
print(str(50.2)) #converting a Float 50.2 to string
print(str(True)) #converting a Bool to string

print(type(str(100)))#converting Int 100 to string And checking it type
print(type(str(50.2))) #converting a Float 50.2 to string  And checking it type
print(type(str(True))) #converting a Bool to string  And checking it type


#ESCAPESEQUENCE

str10 = 'welcome to \'Engineer-D tutorial\'' #Including single quote in a single quote string using escapesequence
print(str10)
str11 = "welcome to \"Engineer-D tutorial\"" #Including double quote in a double quote string using escapesequence
print(str11)

str12 = r'welcome to \'Engineer-D tutorial\'' #Ignoring escapesequence using small r
print (str12)
str13 = R"welcome to \"Engineer-D tutorial\"" #Ignoring escapesequence using capital R
print(str13)

str14 = 'welcome to https:\\Daniel.com\\home' #including \ in a string using escapesequence
print(str14)
str15 = 'welcome to https:\Daniel.com\home' #Ignoring escapesequence
print(str15)

str16 = "print this in a newline \nI am daniel"
print(str16) #Using the newline escapesequence

str17 = "Give me tabspace \tDistance"
print(str17) #Using the tab escapesequence

#STRINGOPERATORS

str18 = "Hello"
str19 = "world"

print(str18+str19) #Adding 2 strings together

print(str18*3)#Multiplying string n-times where n = 3 in this case

print(str18[1]) #printingout the 2nd index
print(str19[0:4]) #printout all the characters before index 5

print("l" in str18) #Checking If L is in str18
print("a" not in str19 ) #checking if A is not in str19

#STRINGSMETHODS

str20 = ' this is daniel '

print(str20.capitalize()) #Making the first letter of str20 uppercase
print(str20.count("s")) #count amount of time S appears in str20
print(str20.endswith("el"))#checking if str20 ends with el
print(str20.find("is"))#Returns the first index of the first occurence of IS.
print(str20.rfind("is")) #Return the last index of the occurence of IS
print(str20.index("n")) #Returns the index of N
print(str20.rindex("i")) #returns the last index of I
print(str20.isalnum())#Check if str20 contains only alpahbets or numbers
print(str20.isalpha())#check if str20 contains only alphabets
print(str20.isdigit()) #check if str20 contais only digit/index
print(str20.isnumeric()) #check if str20 contains only numbers
print(str20.islower()) #check if str20 is all in lowercase
print(str20.isprintable())#check if str20 is printable
print(str20.isupper())#check if str20 is in uppercase
print(str20.istitle()) #checking if each word in str20 has it's first letters in uppercase
print(str20.isspace()) #checking if str20 is all space
print(str20.lower()) #converting str20 to all smaller/lower case
print(str20.upper()) #converting str20 to all capital/upper case
print(str20.title())#converting str20 first letter in each words to capital /uppercase
print(str20.lstrip())#removes leading whitespaces
print(str20.rstrip())#removes trailing whitespaces
print(str20.strip())#removes both leading and trailing whitespace
print(str20.replace("daniel","john"))#replacing Daniel with john
print(str20.split()) #Breaks str20 into component using space
print(str20.startswith("t"))#check if str20 starts with T
print(str20.swapcase())#changing upper case to lower and lower to upper case

strBonus = ' '.join(['10','20','30'])
print(strBonus) #return a string which is the concatenation of each string in the list above

 












































































