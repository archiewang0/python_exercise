import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
array = [rock , paper , scissors]
array_name = ['rock' , 'paper' , 'scissors']

#Write your code below this line 👇

user_choice = int( input('which you choice of those rock type 0 , paper type 1 , scissors type 2 ?') )
computer_choice = random.randint(0,2)

decision = ''
if (user_choice == computer_choice):
    decision = 'a draw !'
else:
    if (user_choice == 0):
        if(computer_choice == 1):
            decision = 'you lose!'
        else:
            decision = 'you win!'
    elif (user_choice == 1):
        if (computer_choice == 0):
            decision = 'you win!'
        else:
            decision = 'you lose!'
    else:
        if (computer_choice == 0):
            decision = 'you lose!'
        else:
            decision = 'you win!'

print(f"""your choice: 
{array[user_choice]} 
{array_name[user_choice]} 

computer choice:
{array[computer_choice]} 
{array_name[computer_choice]} 

{decision}
        """)
