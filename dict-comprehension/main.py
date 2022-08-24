# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# words = sentence.split()
#
# number_of_letters = {word: len(word) for word in words}
#
# print(number_of_letters)

############################################################################

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}

############################################################################

import pandas

data_as_df = pandas.read_csv("nato_phonetic_alphabet.csv")
data_as_dict = {row.letter: row.code for (index, row) in data_as_df.iterrows()}

user_word_uppercase = input("Type the word: ").upper()
word_letters = list(user_word_uppercase)
code_of_letters = []

for letter in word_letters:
    code_of_letters.append(data_as_dict[letter])

print(code_of_letters)




# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

