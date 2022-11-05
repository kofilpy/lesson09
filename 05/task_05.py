import re


# Task 1

def sorted_list(list_sort: list, start_index: int, finish_index: int) -> list:
    """Sorted list between indices"""
    list_sort[start_index:finish_index] = sorted(list_sort[start_index:finish_index])
    return list_sort


print(sorted_list([1, 10, 9, 4, 5, 7, 2, 0], 2, 6))


# Task 2

def calculator(read_file: str) -> str:
    """Calculate examples from the file and write them back"""
    with open(f"{read_file}", 'r') as file:
        file_read = file.read()
    file_calculated = ''
    for row in file_read.split("\n"):
        reg_exp = r'\d+|[+/%()*-]'
        cleaned_row = re.findall(reg_exp, row)
        try:
            calc = f" = {eval(row)}"
        except:
            calc = " - you cannot divide into '0'"
        calculated_row = " ".join(cleaned_row) + calc + "\n"
        file_calculated += calculated_row
    with open(f"{read_file}", 'w') as file:
        file.write(file_calculated)


calculator("file_1.txt")


# Task 3

def palindrome(row: str) -> str:
    """Palindrome definition"""
    cleaned_row = []
    for i in row:
        if i.isalpha() or i.isdigit():
            cleaned_row.append(i.lower())
    cleaned_row_copy = cleaned_row.copy()
    cleaned_row.reverse()
    if cleaned_row == cleaned_row_copy:
        return 'Паліндром'
    else:
        return 'Не паліндром'


print(palindrome("І що сало? Ласощі"))
