import csv


def guide_im_first():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите телефон: ')
    comment = input('Введите описание: ')
    some_list = [last_name, first_name, phone_number, comment]

    with open('guide.txt', 'a', encoding='utf-8') as file:
        file.write(f'{last_name}, {first_name}, {phone_number}, {comment}\n')

    return some_list
