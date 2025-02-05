
# \n 字串斷行
# print('字串斷行: Hello World\nHello World\n')
# # 字串相加
# print('字串相加: Hello'+'World\n')

# # age = input("how old are you?")
# # print('i am '+ age)


# len('test')
# # 4

# print("hello"[2])

# # 列印數字
# print(12312312)

# # 列印large integ
# print(123_12_32_3_5)

# print(3.12321313)

# print(type("hello"))
# print(type(123))
# print(type(123_456_677_777_565))
# print(type(3.14159))

# print( int('123') + int('321'))

# # print('fsdfdsfsfsf' + str(len(input('enter?'))))

# print(3-7)
# print(type(3-7))
# print(3+3)
# print(3/3)
# print(type(3/3))
# print(4//3)
# print(type(4//3)) #取整數
# print(3*2)
# print(3**2) #平方

#運算運作順序
# () 
# ** 
# / OR *
# + OR -
# print(int(30.89))
# print(round(30.89))
# print(round(30.89 , 1)) #小數點後幾位

# number_var = 23132
# bool_var = False
# float_var = 0.421
# print('number: '+ str(number_var))

# # f"" 內使用{} 可以帶入任何變數
# print(f"number: {number_var}")
# print(f"boolean: {bool_var}")
# print(f"float: {float_var}")

# import math

# total = input("總共金額多少錢?")
# split_people = input("多少人分?")
# print(f"總共: { math.ceil(int(total)/ int(split_people))}")


# if bool_var:
#     print('true')
# else:
#     print('false')

# 取餘數
# print(100 % 2)

# height = int(input('how tall you are?'))
# age = int(input('your age? '))
# wanna_take_poto = input('wanna take poto? Yes(y) , No(n)')

# if height > 160:
#     bill = 0

#     if wanna_take_poto == 'y':
#         bill = 50

#     if age > 16:
#         bill = bill + 360
#         print(f"tickt {bill}")
#     elif age < 16 and age >= 10:
#         bill = bill + 280
#         print(f"tickt {bill}")
#     else:
#         bill = bill + 0
#         if bill == 0:
#             print('free tickt')
#         else:
#             print(f"price {bill}")
# else:
#     print('soory , you too Short ! not allow to play this .')


# not只能用在 if else condition中

# import random

# # 10 - 1 之間random integer
# randominteger = random.randint(1, 10)

# # 0 - 1 之間的random 
# random_0_to_1 = random.random()

# # 10 - 1 之間的random float
# radom_uiform = random.uniform(1,10)

# print(radom_uiform)

import random
# taiwan_city = [
# '臺北市',
#   '新北市',
#   '桃園市',
#   '臺中市',
#   '臺南市',
#   '高雄市',
#   '基隆市',
#   '新竹市',
#   '嘉義市',
#   '新竹縣',
#   '苗栗縣',
#   '彰化縣',
#   '南投縣',
#   '雲林縣',
#   '嘉義縣',
#   '屏東縣',
#   '宜蘭縣',
#   '花蓮縣',
#   '臺東縣',
#   '澎湖縣',
#   '金門縣',
#   '連江縣'
# ]

# # -number 則是從 list的尾開始算 -1 倒數第一個
# # 0 則是list 的頭

# taiwan_city[0] = 'taipei city'
# # 加入array
# taiwan_city.append('苗栗國')
# # 合併arrary
# taiwan_city.extend(['new taipei city', 'taichung city'])

# # random 可以隨意選擇 array中其中一個
# # print( random.choice(taiwan_city) )

# # random 另一種方式 , 可以設定選擇範圍
# # random_idx =
# radom_idx = random.randint(0,6)

# list_len = len(taiwan_city) -1
# print( taiwan_city[list_len] )

def format_name(frist_name: str , last_name: str):
    format_first_name =  frist_name.title()
    format_last_name = last_name.title()
    return f"""{format_first_name} {format_last_name}"""


output = format_name(frist_name='aRChIe' , last_name='wAnG')
print(output)