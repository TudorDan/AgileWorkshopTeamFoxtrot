import sys
from view import display
from controller import students_controller


def choose():
    option = display.get_inputs(["Please enter a number: "], "")[0]
    if option == '1':
        students_controller.submenu()
    elif option == '2':
        print("Not implemented yet.")
    elif option == '0':
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    display.print_message("Welcome to Universidad Técnica de Buenas Maneras y Pistoleros!")
    main_options = ["Exit program",
                    "School Students",
                    "Statistics"]
    display.print_menu("Main Menu", main_options)


def menu():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            display.print_message(str(err))
