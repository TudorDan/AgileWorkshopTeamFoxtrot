def get_table_from_file(file_name):
    """
    Reads csv file and returns it as a list of lists.
    Lines are rows columns are separated by ";"
    :param file_name: name of file to read
    :return: list: list of lists read from a file.
    """
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            return [element.replace("\n", "").split(";") for element in lines]
    except IOError as err:
        print(err)
        return []


def write_table_to_file(file_name, table):
    """
    Appends list of lists into a csv file.
    :param file_name: name of file to write to
    :param table: list of lists to write to a file
    :return: None
    """
    with open(file_name, "a+") as file:
        for record in table:
            row = ';'.join(record)
            file.write(row + "\n")


def get_number_of_students():
    students = 0
    for row in open("model/files/students.csv"):
        students += 1
    return students
