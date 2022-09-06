def printMainMenu():
    print("Выберите пункт меню:\n \
    1 - поиск телефона по имени\n \
    2 - добавление записи\n \
    3 - печать справочника\n \
    4 - перенос справочника в html-файл")

def getValues():
    user_input = input("Напишите ответ: ")
    return int(user_input)

def input_name():
    name = input("Введите имя для поиска ")
    return name

def print_no_find_mess(name):
    print(f'Аббонент {name} отсутсвует в справочнике')

def input_new_data():
    data = input("Введите новую запись для справочника ")
    return data

def print_all(directory):
    print(directory)

def errorMessage():
    print("Нет такого пункта меню")