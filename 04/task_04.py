# Task 1

list_test = [10, 25, 4, 16, 12569, 100500, 1, 16, 8, 76]
# a
list_pair_index = list_test[::2]
# list_pair_index = [list_test[i] for i in range(len(list_test)) if i % 2 == 0]
print(list_pair_index)

# b
list_sum = sum(list_test)
print(list_sum)

# c
list_pair_sum = sum(list_pair_index)
print(list_pair_sum)
list_unpair_sum = list_sum - list_pair_sum
print(list_unpair_sum)

# d
list_max_el = max(list_test)
list_max_el_index = list_test.index(list_max_el)
print(list_max_el, list_max_el_index, sep="\n")


# Task 2
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


def fizzbuzz_read():
    """Кодування для чисел з файлу"""
    with open("file_1.txt", 'r') as file:
        file_read = file.read()
    fizzbuzz_list = []
    for row in file_read.split('\n'):
        fizz, buzz, number = map(int, row.split())
        fizzbuzz_row = fizz_buzz(fizz, buzz, number)
        fizzbuzz_list.append(fizzbuzz_row)
    return '\n'.join(fizzbuzz_list)


print(fizzbuzz_read())


# Task 3
def sorted_list(list_unsorted: list) -> list:
    """Сортування по 5 елементів в списку"""
    for i in range(len(list_unsorted) // 5 + 1):
        list_unsorted[i * 5:i * 5 + 5] = sorted(list_unsorted[i * 5:i * 5 + 5])
        if i % 2 == 1:
            list_unsorted[i * 5:i * 5 + 5] = list_unsorted[i * 5:i * 5 + 5][::-1]
    return list_unsorted


list_unsorted = [32, 43, 1, 3, 4, 5, 34, 5, 1, 7, 10, 34, 17, 11, 7, 10, 34, 17, 11, 56]
sorted_list1 = sorted_list(list_unsorted)
print(sorted_list1)
# [1, 3, 4, 32, 43, 34, 7, 5, 5, 1, 7, 10, 11, 17, 34, 56, 34, 17, 11, 10]
