from view import display
from model import data_manager


def get_all_students():
    students = data_manager.get_table_from_file("model/files/students.csv")
    display.print_table(students, "Students List:")


def get_all_students_per_class():
    students_class = {}
    students = data_manager.get_table_from_file("model/files/students.csv")
    for student in students:
        if student[1] in students_class:
            students_class[student[1]] += 1
        else:
            students_class.update({student[1]: 1})
    print("Number of students per class:")
    for items in students_class.items():
        print(items)


def choose_operation():
    option = display.get_inputs(["Please enter a number: "], "")[0]
    if option == '1':
        get_all_students()
    elif option == '2':
        display.print_message("Add", True)
    elif option == '3':
        display.print_message("Update", True)
    elif option == '4':
        display.print_message("Delete", True)
    elif option == '5':
        get_all_students_per_class()
    elif option == '0':
        return False
    else:
        raise KeyError("There is no such option.")
    return True


def handle_submenu():
    options = ["Exit submenu",
               "List students",
               "Add a new student",
               "Update student",
               "Delete student",
               "Number of students per class"]
    display.print_menu("Student Classes Submenu", options)


def submenu():
    running = True
    while running:
        handle_submenu()
        try:
            running = choose_operation()
        except KeyError as err:
            display.print_message(str(err), True)
