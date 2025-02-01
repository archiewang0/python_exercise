# taiwan_city = [
# '臺北市',
#   '新北市',
#   '連江縣'
# ]

# for city in taiwan_city:
#     print(city)
# print(taiwan_city)

# sum (number[]) => totalNummber: number
numbers = [ 1, 2, 3,4,5 ,6, 7, 8, 9,10 ,33, 43,66]
# print(sum(numbers))

# sum = 0
# for num in numbers:
#     sum = sum+ num
# print(sum)

# print(max(numbers))

# max = 0
# for num in numbers:
#     if (num > max):
#         max = num
# print(max)

# print(range(1,10))
# range( startNum , endNum ) 回傳 number[]
# for num in range(1,10):
#     print(num)

# total = 0
# for num in range(1,100):
#     total = total + num

# print(total)



#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
# password = ''
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# for run in range(0 ,nr_letters ):
#     password = password + random.choice(letters)

# for run in range(0 ,nr_numbers ):
#     password = password + random.choice(numbers)

# for run in range(0 ,nr_symbols ):
#     password = password + random.choice(symbols)

# print(f"""there is your password! {password}""")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
passwordList = []
for run in range(0 ,nr_letters ):
    passwordList.append(random.choice(letters)) 

for run in range(0 ,nr_numbers ):
    passwordList.append(random.choice(numbers)) 


for run in range(0 ,nr_symbols ):
    passwordList.append(random.choice(symbols)) 

random.shuffle(passwordList)
password = ''
for item in passwordList:
    password = password + item

print(password)