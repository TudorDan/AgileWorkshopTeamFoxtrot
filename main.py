from controller import enigma


def print_hi(name):
    """

    :param name:
    :return:
    """
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    file = open("model/files/decrypted.txt", "rt")
    data = file.readlines()
    file.close()
    print(data)

    with open("model/files/encrypted.txt", "rt") as file2:
        data2 = file2.read()
        print(data2)


print_hi('PyCharm')
enigma.show_menu()
