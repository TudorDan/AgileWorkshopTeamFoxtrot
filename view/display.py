RESET = "\033[0;0m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
PURPLE = "\033[1;35m"
CYAN = "\033[1;36m"


def print_menu(title, list_options):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) School Students
            (2) Statistics
            (0) Exit program
    :param title: menu title
    :param list_options: list of strings - options that will be shown in menu
    :return: None: This function doesn't return anything it only prints to console.
    """
    print(f"{PURPLE}{title}{RESET}")
    for index, option in enumerate(list_options):
        print(f"({index}) {option}")


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","School Class","Subject"],
                   "Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        School Class <user_input_2>
        Subject <user_input_3>
    :param list_labels: labels of inputs
    :param title: title of the "input section"
    :return: list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    print(f"{YELLOW}{title}{RESET}")
    for item in list_labels:
        inputs.append(input(f"{item}"))
    return inputs


def print_message(message, error=False):
    """
    Displays a message (example: ``@message``)
    :param error: optional true for error messages
    :param message: string to be displayed
    :return: None: This function doesn't return anything it only prints to console.
    """
    if error:
        print(f"{RED}{message}{RESET}")
    else:
        print(f"{GREEN}{message}{RESET}")


def print_table(table, title):
    """
    Displays data from files
    :param table: List of lists - the table to print out
    :param title: Title of the table for printing
    :return: None: This function doesn't return anything it only prints to console.
    """
    print(f"{CYAN}{title}{RESET}")
    headers = table[0]
    for i in range(1, len(table)):
        for index, column in enumerate(table[i]):
            print(f"{headers[index]}:{BLUE}{column}{RESET} ", end="")
        print("\n----------------------------------------")
