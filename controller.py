import model_find_name
import model_new_data
import model_print_all
import model_html
import view

def call_model_find_name():
    tel = model_find_name.read_file()
    person = view.input_name()
    fl = model_find_name.find_name(tel, person)
    if fl == True:
        view.print_no_find_mess(person)

def call_model_new_data():
    new_data = view.input_new_data()
    model_new_data.adding_data(new_data)

def call_model_print_all():
    direc = model_print_all.read_file()
    view.print_all(direc)

def call_model_html():
    tel = model_find_name.read_file()
    model_html.create_html(tel)

value = None
def initValues():
    global value
    value = view.getValues()

def buttomClick():
    global value
    if value == 1:
        call_model_find_name()
    elif value == 2:
        call_model_new_data()
    elif value == 3:
        call_model_print_all()
    elif value == 4:
        call_model_html()
    else:
        view.errorMessage()
