logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

def add(n1 , n2):
    return n1+n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 - n2

def divide(n1 , n2):
    return n1 / n2

operation_object = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
} 


first_ask_number =  int(input('What is your first number?'))

def ask_calc_number(n1):
    number1 = n1
    for key in operation_object:
        print(key)
    operation = input('Pick a operation?')
    next_number =  int(input('What is next number?'))
    result = operation_object[operation](number1, next_number)
    print(f"""{number1} {operation} {next_number} = {result}""")

    continue_input = input('Do you want to keep number , continue to calc ? yes(y) no(n)')

    if continue_input == 'y':
        ask_calc_number(result)
    else:
        print('finish!')



ask_calc_number(first_ask_number)

