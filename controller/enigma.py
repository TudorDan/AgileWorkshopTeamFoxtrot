from view import display
from model import cipher_factory


def show_menu():
    display.print_menu()


def handle_args(arguments):
    """
    Validates given arguments and then invokes handle_cipher_operation
    :param arguments: Command line arguments
    """
    # TODO: Command line arguments validation

    handle_cipher_operation(arguments)


def handle_cipher_operation(arguments):
    cipher_factory.get_cipher_for_args(arguments)

    # TODO: Use cipher
