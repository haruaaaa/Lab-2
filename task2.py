from csv import reader

while True:
    flag = 0 #метка на колво по поиску с ограничением
    search = input('Введите запрос: ')
    if search == '0':
        break
    with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        for row in table:
            lower_case = row[2].lower()
            index = lower_case.find(search.lower())
            row[6] = row[6].replace(',','.')
            if index != -1 and float(row[6])<200:
                print(row[1])
                flag += 1

        if flag == 0:
            print('Ничего не найдено.')
        else:
            print(f'Найдено {flag} результатов.')
