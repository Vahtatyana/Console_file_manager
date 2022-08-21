import os
import shutil
import Vactory
import Bank


def list_dir(a = 1):
    l_dir = os.listdir()
    for i in l_dir:
        if a == 1:
            print(i)
        elif os.path.isdir(i) and a == 2:
            print(i)
        elif os.path.isfile(i) and a == 3:
            print(i)

while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папкии')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной систем')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход')

    choice = input('Выберите пункт меню')
    if choice == '1':
        name_dir = input('Введите имя папки:')
        if not os.path.exists(name_dir):
            os.mkdir(name_dir)
            print(f'Папка {name_dir} создана.')
        else:
            print(f'Папка {name_dir} уже существует.')
    elif choice == '2':
        name_dir = input('Введите имя папки или файла: ')
        if  os.path.exists(name_dir) and os.path.isdir(name_dir):
            os.rmdir(name_dir)
            print(f'Папка {name_dir} удалена.')
        elif  os.path.exists(name_dir) and os.path.isfile(name_dir):
            os.remove(name_dir)
            print(f'Файл {name_dir} удален.')
        else:
            print(f'Папки или файла {name_dir} не существует.')
    elif choice == '3':
        name_dir = input('Введите имя папки или файла: ')
        new_name_dir = input('Введите новое имя папки или файла: ')
        shutil.copytree(name_dir, new_name_dir)
        print(f'Папка {name_dir} скопирована. ')
    elif choice == '4':
        list_dir()
    elif choice == '5':
        list_dir(2)
    elif choice == '6':
        list_dir(3)
    elif choice == '7':
        print(os.name)
    elif choice == '8':
        print('Создатель программы: Вахрушева ТС')
    elif choice == '9':
        Vactory.game()
    elif choice == '10':
        Bank.bill()
    elif choice == '11':
        path = input('Введите новый путь:')
        os.chdir(path)
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')
