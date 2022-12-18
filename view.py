def choice():
    some_str = input(
        'Введите "0" (чтобы сделать запись в справочнике), или введите "1" (чтобы получить запись из справочника): ')
    return some_str


def view_data_im(data):
    print(f'\nСоздана запись:')
    print(f'*{", ".join(data)}')


def view_data_ex(request, data):
    if data != "":
        print(f'\nПо запросу "{request}" получены записи:')
        for i in data:
            print(f'*{i}')
    else:
        print(f'\nПо запросу "{request}" записи не найдены')
