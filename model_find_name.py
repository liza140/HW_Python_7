# Задача 1. Создайте телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
# Предусмотрите следующие функции для справочника:
# - новая запись; - вывод всего справочника; - поиск по имени;
# - экспорт справочника в форматы html, xml; - чтение данных из файла; - дополнительные функции по желанию
# Требуется реализовать минимум 3 инструмента для работы со справочником.

def read_file():
    with open('telefons.txt', "r", encoding='utf-8') as file:
        tel_directory = file.read()
        tel_directory = tel_directory.split("\n")
    return tel_directory

    
def find_name(tel_directory, Name): 
    flag = True
    for str in tel_directory:
        if Name in str:
            print(str)
            flag = False
    return flag

