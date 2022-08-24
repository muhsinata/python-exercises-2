sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()

number_of_letters = {word: len(word) for word in words}

print(number_of_letters)
