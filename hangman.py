#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]


chosen_word = random.choice(word_list)
chosen_word_len = len(chosen_word)

placeholder = ''
for run in range(0,chosen_word_len):
    placeholder += ' _'

print('guess a letter of word: '+placeholder)
# chosen_word_list = list(chosen_word)

guess_letter = input('guess a letter, must be one of the letters in the chosen word?').lower()


result = ''
for letter in chosen_word:
    if ( letter == guess_letter):
        result += ' '+letter
    else:
        result += ' _'

print(chosen_word)
print(guess_letter)
print(result)
# if ( guess_letter in chosen_word ):
#     print('ok')
# else:
#     print('error')