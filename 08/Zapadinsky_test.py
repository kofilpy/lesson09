# # 1
# string = input()
# h1 = string.find('h')
# h2 = string.rfind('h')
# new_string = string[h1+1:h2]
# new_string = new_string[::-1]
# print(new_string)

# #2
# string = input()
# str_big = 0
# str_little = 0
# str_digit = 0
# for i in string:
#     if i.isupper():
#         str_big += 1
#     elif i.islower():
#         str_little += 1
#     elif i.isdigit():
#         str_digit += 1
# str_other = len(string) - str_big - str_little - str_digit
# print([str_big, str_little, str_digit, str_other])
#
# # 3
# string = input()
# number_list = []
# for i in string:
#     if i.isdigit():
#         number_list.append(int(i))
# print(number_list)

# # 4
# def change_str(string: str):
#     space_numbers = string.count(' ')
#     new_string = string.replace(' ', '', space_numbers - 1)
#     return new_string
#
#
# string = 'Simple, remove the spaces from the string'
# print(change_str(string))
#
# # 5
# def create_str(str_list: list):
#     str_from_list = " ".join([str(i) for i in str_list])
#     return str_from_list
#
#
# str_list = [32, 4.43, 'lister', False, None, [1, 2, 3, 4]]
# print(create_str(str_list))

# # 6
# country_dict = {
#     'Ukraine': 'Kyiv',
#     'Australia': 'Canberra',
#     'Austria': 'Vienna',
#     'Brazil': 'Brasilia',
#     'Canada': 'Ottawa',
#     'Colombia': 'Bogota',
#     'Cuba': 'Havana',
#     'Denmark': 'Copenhagen',
#     'Egypt': 'Cairo',
#     'France': 'Paris',
# }
# capital = input()
# while capital != 'стоп':
#     answer = ''
#     for country in country_dict:
#         if capital in country_dict[country]:
#             print(f'так це столиця {country}')
#             break
#         else:
#             print("ні, на жаль це не столиця")
#             break
#     capital = input()

# # 7
#
# def dictionary_change(dictionary: dict):
#     new_dict = {}
#     for key, value in dictionary.items():
#         if isinstance(value, str):
#             new_dict[value] = [key]
#         else:
#             for i in value:
#                 if i in new_dict:
#                     new_dict[i].append(key)
#                 else:
#                     new_dict[i] = [key]
#     return new_dict
#
#
# dictionary = {"apple": ['malum', 'omum', 'popula'], 'fruit': ['baca', 'bacca', 'popum'], 'punishment': ['malum', 'multa'], 'dog': 'canina'}
# print(dictionary_change(dictionary))
#

# # 8
#
# def repeat_self(string):
#     i = (string + string).find(string, 1, -1)
#     return False if i == -1 else True
#
#
# print(repeat_self("aaaa"))


# # 9
#
# def is_colon(string):
#     string = "".join(i for i in string if i in "〈({[]})〉")
#     while string:
#         answer = True
#         for i in "〈〉", "()", "{}", "[]":
#             if i in string:
#                 string = string.replace(i, "")
#                 answer = False
#         if answer:
#             return False
#     return True
#
#
# string = "[({})](]"
# print(is_colon(string))


# # 10
#
# with open('file_1.txt', 'r') as file:
#     file_read = file.read()
# file_c = file_read.replace('\n', ' ')
# file_list = file_c.split(' ')
# max_length_word = ''
# for i in file_list:
#     if len(i) > len(max_length_word):
#         max_length_word = i
# max_length_word_up = max_length_word.upper()
# new_file = file_read.replace(max_length_word, max_length_word_up)
# with open('file_1.txt', 'w') as file:
#     file.write(new_file)
#


