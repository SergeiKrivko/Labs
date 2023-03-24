import os
from menu import menu
from in_out import input_value


pos_tests = []
neg_tests = []

lab_number = input_value("Введите номер лабы", int, only_positive=True)
task_number = input_value("Введите номер задачи", int, only_positive=True)
var = input_value("Введите номер варианта", int)
input_values = input("Введите входные данные: ")
output_values = input("Введите выходные данные: ")

path = f'/home/sergei/C_labs/iu7-cprog-labs-2023-krivkosergei/lab_{lab_number:0>2}_{task_number:0>2}_{var:0>2}'


def add_test(tests):
    description = input()

    lst = []
    while s := input():
        lst.append(s)
    test = '\n'.join(lst) + '\n'
    tests.append((description, test))


def generate_test(index, type='pos'):
    os.makedirs(f"{path}/func_tests/data", exist_ok=True)

    tests = pos_tests if type == 'pos' else neg_tests
    file_in = open(f"{path}/func_tests/data/{type}_{index + 1:0>2}_in.txt", "w")
    file_in.write(tests[index][1])
    file_in.close()

    os.system(f"{path}/app.exe < {path}/func_tests/data/{type}_{index + 1:0>2}_in.txt > "
              f"{path}/func_tests/data/{type}_{index + 1:0>2}_out.txt")


def save_tests():
    print("Compiling...")
    os.system(f"gcc -std=c99 -Wall -Werror -Wvla {path}/main.c -o {path}/app.exe -lm")

    readme = open(f"{path}/readme.md", 'w', encoding='utf-8')
    readme.write(f"# Тесты для лабораторной работы №{lab_number:0>2}, задания №{task_number:0>2} \n\n "
                 f"## Входные данные\n{input_values}\n\n"
                 f"## Выходные данные\n{output_values}\n\n"
                 f"## Позитивные тесты:\n")
    for i in range(len(pos_tests)):
        readme.write(f"- {i + 1:0>2} - {pos_tests[i][0]}\n")
        generate_test(i, 'pos')

    readme.write("\n## Негативные тесты:\n")

    for i in range(len(neg_tests)):
        readme.write(f"- {i + 1:0>2} - {neg_tests[i][0]}\n")
        generate_test(i, 'neg')

    exit(0)


menu(('Добавить позитивный тест', lambda: add_test(pos_tests)),
     ('Добавить негативный тест', lambda: add_test(neg_tests)),
     ('Завершить создание тестов', save_tests))


os.system(f"{path}/app.exe")

