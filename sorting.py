students = [('Bob Mac', 39), ('Joe Acer', 26), ('Jimmy Lenovo', 40)]


def sort_key(student):
    return student[0].split(" ")[1]


sorted(students, key=sort_key)
