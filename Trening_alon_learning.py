documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
}


while True:
    numbers = input('Нажмите "p"/"s"/"l"/"a" для заупуска команды. Для завершения нажмите "q" ')
    if 'q' in numbers:
        break

    elif 'p' in numbers:
        number_doc = input('Введите номер документа для вывода имени человека ')
        def people():
            '''команда, которая спросит номер документа и выведет имя человека, которому он принадлежит'''
            for doc in documents:
                if number_doc == doc['number']:
                    doc_name = doc['name']
            return doc_name
        print(people())


    elif 's' in numbers:
        shelf_doc = input('Введите номер документа для вывода номера полки ')
        def shelf():
            '''команда, которая спросит номер документа и выведет номер полки, на которой он находится'''
            for doc in documents:
                if shelf_doc == doc['number']:
                    for key, value in directories.items():
                        if shelf_doc in value:
                            shelf_doc_ = key
            return shelf_doc_
        print(shelf())

    elif 'l' in numbers:
        def lists():
            '''команда, которая выведет список всех документов '''
            all_list = []
            adds = []
            for all in documents:
                list_ = (f' {all["type"]} "{all["number"]}" "{all["name"]}"')
                print(list_)
            return list_
        lists()


    if 'a' in numbers:
        def add():

            ''' команда, которая добавит новый документ в каталог и в перечень полок,
            спросив его номер, тип, имя владельца и номер полки,
            на котором он будет храниться.
            '''

            a = input('Введите данные ч/з запятую порядке:type, number, name ')
            b = int(input('Введите в номер директории где необходимо разместить номер '))
            if b > 3:
                print('Директории не существует. Доступные: 1, 2, 3')
                b = int(input('Введите в номер директории где необходимо разместить номер '))
            a = a.split(',')
            doc_all = {'type':a[0], 'number': a[1], 'name': a[2]}
            documents.append(doc_all)


            directories[str(b)] = a[1]
            return directories

        print(add())