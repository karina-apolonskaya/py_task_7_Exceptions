# #Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:
# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
# n - выводит имена владельцев документов

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006', '5400 028765', '5455 002299'],
        '3': []
      }

# # p – people
def get_doc_number(documents):
    user_doc_number = input("Введите номер документа:"'\t')
    number_keeper = ""
    for document in documents:
        if document["number"] == user_doc_number:
            number_keeper = document["name"]
    if number_keeper == "":
        print("Такого номера нет в базе данных! Попробуйте еще раз!")
    else:
        print(f"Человек, которому принадлежит документ:\t{number_keeper}")

# get_doc_number(documents)

# #l– list
def get_all_docs(documents):
    for document in documents:
        print(document["type"], document["number"], document["name"])

# # get_all_docs(documents)

# #s – shelf
def get_shelf_number(directories):
    user_doc_number_1 = input("Введите номер документа:"'\t')
    shelf_number = ""
    for directory in directories:
        if user_doc_number_1 in directories[directory]:
            shelf_number = directory
    if shelf_number != "":
        print(f"Номер полки: \t {shelf_number}")
    else:
        print("Такого номера нет в базе! Попробуйте еще раз!")       
# # get_shelf_number(directories)

# # a – add 
# def add_document_to_shelf(documents, directories):

    doc_number = input("Введите номер документа:" "\t")
    doc_type = input("Введите тип документа:" "\t")
    name = input("Введите ваше имя:" "\t")
    shelf_number = input("Введите номер полки:" "\t")
    shelf_counter = ""

    for directory in directories:
        if shelf_number in directories:
            shelf_counter = directory
    if shelf_counter == "":
        print("\nТакой полки у нас не существует! Попробуйте еще раз!")
    else:
        print(f"\nДокумент добавлен на полку: {shelf_number}""\n")
        directories[shelf_number].append(doc_number)
        print(directories)
        documents.append({"type": doc_type, "number": doc_number, "name": name})
        print(documents)
            
# add_document_to_shelf(documents, directories) 

#n - names
def print_all_names(documents):
    try:
        for document in documents:
            document_number = document["number"]
            print(document["name"])
    except KeyError:
        print(f"У документа с номером {document_number} нет поля 'name'")

# print_all_names(documents)


def get_command(documents, directories):
    user_command = input("Введите одну из возможных команд - p, l, s, a, n :" "\t" )
    print()
    if user_command == 'p':
        get_doc_number(documents)
    elif user_command == 'l':
        get_all_docs(documents)
    elif user_command == 's':
        get_shelf_number(directories)
    elif user_command == 'a':
        add_document_to_shelf(documents, directories)
    elif user_command == 'n':
        print_all_names(documents)

get_command(documents, directories) 