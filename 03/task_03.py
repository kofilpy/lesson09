# Task 1
def three_rows_middle(rows):
    """Виведення на екран середини рядка"""
    middle_rows = []
    for row in rows:
        length = len(row)
        middle_length = int(length / 2)
        if length % 2:
            middle_part = row[middle_length]
        else:
            middle_part = row[middle_length - 1:middle_length + 1]
        middle_rows.append(middle_part)
    return middle_rows


rows = [input() for i in range(3)]
three_rows_middle1 = three_rows_middle(rows)
[print(i) for i in three_rows_middle1]


# Task 2
def row_change(row: str) -> str:
    """Операції з рядками1"""
    if 5 <= len(row) <= 15:
        new_row = row[:-3] + row[-3:].upper()
        middle_length = int(len(new_row) / 2)
        new_row = new_row[middle_length:] + new_row[:middle_length]
        return new_row
    else:
        return "Введіть рядок, розмір якого не менше 5 символів і не більше 15"


row = input()
row_change1 = row_change(row)
print(row_change1)


# Task 3
def row_new_change(row: str) -> str:
    """Операції з рядками2"""
    if len(row) <= 10:
        first_part, last_part = row[:-3], row[-3:].lower()
        middle_length = int(len(first_part) / 2)
        new_row = first_part[:middle_length] + last_part + first_part[middle_length:]
        return new_row
    else:
        return "Введіть рядок розміром не більше 10 символів"


row = input()
row_new_change1 = row_new_change(row)
print(row_new_change1)


# Task 4
def hashtag_square(side: int):
    """Квадрат з хеш-тегів"""
    for i in range(1, side + 1):
        if i == 1 or i == side:
            [print("#", end="") for i in range(side)]
            print("")
        else:
            print("#", end="")
            [print(" ", end="") for i in range(1, side - 1)]
            print("#", end="")
            print("")


side = int(input())
hashtag_square1 = hashtag_square(side)
hashtag_square1
