import os
import shutil

while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной систем')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        name_dir = input('Введите имя папки:')
        if not os.path.exists(name_dir):
            os.mkdir(name_dir)
            print(f'Папка {name_dir} создана.')
        else:
            print(f'Папка {name_dir} уже существует.')

    elif choice == '2':
        name_dir = input('Введите имя папки или файла: ')
        if os.path.isdir(name_dir):
            try:
                os.rmdir(name_dir)
                print('Папка удалена!')
            except OSError:
                print('Папка не пуста!')
        elif os.path.isfile(name_dir):
            os.remove(name_dir)
            print('Файл удален!')
        else:
            print('Файл/папка не найден!')

    elif choice == '3':
        name_dir = input('Введите имя папки или файла: ')
        new_name_dir = input('Введите новое имя папки или файла: ')
        shutil.copytree(name_dir, new_name_dir)
        print(f'Папка {name_dir} скопирована. ')

    elif choice == '4':
        if len(os.listdir()) == 0:
            print('Директория пуста!')
        else:
            print(os.listdir())

    elif choice == '5':
        for i in os.listdir():
            if os.path.isdir(i):
                print(i)

    elif choice == '6':
        for i in os.listdir():
            if os.path.isfile(i):
                print(i)

    elif choice == '7':
        print(os.name)

    elif choice == '8':
        print('Создатель программы: Вахрушева ТС')
    elif choice == '10':
        import Bank
        Bank.bill()
    elif choice == '9':
        import Vactory
        Vactory.game()
    elif choice == '11':
        path = input('Введите новый путь:')
        os.chdir(path)

    elif choice == '12':
        print(f'Текущая рабочая директория: {os.getcwd()}')
        directory = input('Введите название директории или путь:  ')
        os.chdir(directory)
    else:
        print ("Неверный пункт меню")