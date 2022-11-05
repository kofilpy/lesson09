# Task 1
def leap_year(year: int) -> str:
    """Визначення, чи є рік високосним"""
    if year % 400 == 0 or year % 4 == 0 and year % 100:
        return 'YES'
    else:
        return 'NO'


year = int(input("Введіть рік: "))
leap_year1 = leap_year(year)
print(leap_year1)


# Task 2
def leap_year(year: int) -> str:
    """Визначення, чи є рік високосним"""
    if not year % 400:
        return 'YES'
    elif not year % 4 and year % 100:
        return 'YES'
    else:
        return 'NO'


year = int(input("Введіть рік: "))
leap_year1 = leap_year(year)
print(leap_year1)


# Task 3
def fizz_buzz(fizz: int, buzz: int, number: int) -> str:
    """Кодування порядку чисел"""
    str_list = []
    for i in range(1, number + 1):
        if i % fizz == 0 and i % buzz == 0:
            str_list.append("FB")
        elif i % fizz == 0:
            str_list.append("F")
        elif i % buzz == 0:
            str_list.append("B")
        else:
            str_list.append(str(i))
    str_list_formatted = " ".join(str_list)
    return str_list_formatted


fizz, buzz, number = map(int, input("Введіть 3 числа: ").split())
fizz_buzz1 = fizz_buzz(fizz, buzz, number)
print(fizz_buzz1)
