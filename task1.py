from csv import reader

with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    flag2 = 0 #метка на количество названий более 30 символов
    for row in table:
        if len(row[1])>30:
            flag2 +=1

    if flag2 ==0:
        print('Нет книг с названиями больше 30 символов.')
    else:
        print(f'Найдено {flag2} книг с названиями более 30 символов.')
