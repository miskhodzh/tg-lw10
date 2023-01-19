# Задание 1
# Решить индивидуальное задание лабораторной работы 8, оформив каждую команду в виде
# отдельной функции.

students = []

def journal():
    f = 0
    for x in students:
        s = 0
        for y in x['academic_performance']:
            s += int(y)
        if s/5 > 4:
            f += 1
            print(x['name'], x['group'])
    if f == 0:
        print('Нет студентов со средним балом выше 4.0')

def add():
    name = input('Введите Фамилию и инициалы > ')
    group = input('Введите номер группы > ')
    academic_performance = input('Введите пять оценок (через ",") > ').split(',')

    student = {
        'name': name,
        'group': group,
        'academic_performance':academic_performance
    }
    students.append(student)
    students.sort(key=lambda item: item.get('group', ''))

print('Введите help для вывода списка команд')
while 1:
    command = input('>>> ').lower()

    if command == 'exit':
        break
    
    elif command == 'add':
        add()
    
    elif command == 'list':
        journal()
    
    elif command == 'help':
        print('add - добавить данные')
        print('list - список студентов со средним баллом выше 4.0')
        print('exit - завершить работу программы')