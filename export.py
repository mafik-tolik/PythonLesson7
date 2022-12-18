import csv


def guide_ex_first():
    some_guide = []
    request = input('Введите данные для поиска: ')
    with open('guide.txt', 'r', encoding='utf-8') as file:
        some_list = file.read().splitlines()
        for i in range(len(some_list)):
            if request in some_list[i]:
                some_guide.append(some_list[i])

    return request, some_guide
