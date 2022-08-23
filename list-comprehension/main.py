# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [number ** 2 for number in numbers]
# even_numbers = [number for number in numbers if number % 2 == 0]
#
# print(squared_numbers)
# print(even_numbers)

######################################################################

with open("file1.txt") as file_1:
    file_1_numbers = file_1.read().splitlines()

with open("file2.txt") as file_2:
    file_2_numbers = file_2.read().splitlines()

common_numbers = [int(number) for number in file_1_numbers if number in file_2_numbers]

print(common_numbers)