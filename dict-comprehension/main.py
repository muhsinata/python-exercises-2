# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# words = sentence.split()
#
# number_of_letters = {word: len(word) for word in words}
#
# print(number_of_letters)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}
