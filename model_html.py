# Задача 1. Создайте телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
# Предусмотрите следующие функции для справочника:
# - новая запись; - вывод всего справочника; - поиск по имени;
# - экспорт справочника в форматы html, xml; - чтение данных из файла; - дополнительные функции по желанию
# Требуется реализовать минимум 3 инструмента для работы со справочником.


def create_html(tel_directory):
    style = 'style="front-size:30px"'
    html = '<html>\n <head></head>\n <body>\n'
    for str in tel_directory:
        html += '<p {}> {}</p>\n'\
        .format(style, str)
    html += '</body>\n</html>'

    with open('index.html', "w") as page:
        page.write(html)

    return html