text = 'Отец мой Андрей Петрович Гринев в молодости своей служил при графе Минихе \
и вышел в отставку премьер-майором в -1700 + 43 году. С тех пор жил он в своей \
Симбирской деревне, где и женился на девице Авдотье Васильевне Ю., дочери \
бедного тамошнего дворянина. Нас было девять человек детей. Все мои братья \
и сестры умерли во младенчестве. Матушка была еще мною брюхата, как уже я \
был записан в Семеновский полк сержантом, по милости майора гвардии князя В., \
близкого нашего родственника. Если бы паче всякого чаяния матушка родила дочь, \
то батюшка объявил бы куда следовало о смерти неявившегося сержанта, и дело \
тем бы и кончилось. Я считался в отпуску до окончания наук. В то время \
воспитывались мы не по-нонешнему. С пятилетнего возраста отдан я был на \
руки стремянному Савельичу, за трезвое поведение пожалованному мне в \
дядьки. Под его надзором на двенадцатом году выучился я русской грамоте \
и мог очень здраво судить о свойствах борзого кобеля. В это время батюшка \
нанял для меня француза, мосье Бопре, которого выписали из Москвы вместе с\
годовым запасом вина и прованского масла. Приезд его сильно не понравился Савельичу.'


def split_to_rows(st, max_width):



def print_text(txt):
    print()
    for st in txt:
        print(st)


def left_alignment(txt):
    max_len = 0
    remove_space(txt)
    for i in range(len(txt)):
        txt[i] = txt[i].strip()
        max_len = max(max_len, len(txt[i]))
    for i in range(len(txt)):
        txt[i] = '{0:<{1}}'.format(txt[i], max_len)


def right_alignment(txt):
    max_len = 0
    remove_space(txt)
    for i in range(len(txt)):
        max_len = max(max_len, len(txt[i]))
    for i in range(len(txt)):
        txt[i] = '{0:>{1}}'.format(txt[i], max_len)


def width_alignment(txt):
    max_len = 0
    remove_space(txt)
    for i in range(len(txt)):
        max_len = max(max_len, len(txt[i]))
    for i in range(len(txt)):
        lst = txt[i].split()
        old_count = len(lst) - 1
        if old_count:
            new_count = max_len - len(txt[i])
            s = ''
            for j in range(len(lst)):
                if new_count % old_count > j:
                    s += lst[j] + ' ' * (2 + new_count // old_count)
                else:
                    s += lst[j] + ' ' * (1 + new_count // old_count)
            txt[i] = s
        else:
            txt[i] = '{0:^{1}}'.format(txt[i], max_len)


def remove_space(txt):
    for i in range(20, 1, -1):
        for j in range(len(txt)):
            txt[j] = txt[j].replace(' ' * i, ' ')


def remove_word_from_text(txt):
    def remove_word(txt, word):
        for i in range(len(txt)):
            txt[i] = txt[i].replace(' ' + word + ' ', ' ')

    word = input('Введите слово для удаления: ')
    remove_word(txt, word)


def replace_word_in_text(txt):
    def replace_word(txt, word1, word2):
        for i in range(len(txt)):
            txt[i] = txt[i].replace(' ' + word1 + ' ', ' ' + word2 + ' ')

    word1 = input('Введите заменяемое слово: ')
    word2 = input('Введите новое слово: ')
    replace_word(txt, word1, word2)


def calculations(txt):
    for j in range(len(txt)):
        a = txt[j].split()
        i = 0
        while i < len(a) - 2:
            if a[i] == '+':
                if a[i - 1].isdecimal() and a[i + 1].isdecimal():
                    a[i] = str(int(a[i - 1]) + int(a[i + 1]))
                    a.pop(i + 1)
                    a.pop(i - 1)
            elif a[i] == '-':
                print(1)
                if a[i - 1].isdecimal() and a[i + 1].isdecimal():
                    print(2)
                    a[i] = str(int(a[i - 1]) - int(a[i + 1]))
                    a.pop(i + 1)
                    a.pop(i - 1)
            else:
                i += 1
        txt[j] = ''
        for el in a:
            txt[j] += el + ' '


def find_and_remove_sentence(txt):
    def convert_text_to_sentences(txt):
        lst = []
        t = []
        for i in range(len(txt) - 1):
            last_point = 0
            for j in range(1, len(txt[i])):
                if txt[i][j - 1] in '.!?' and txt[i][j] == ' ' and txt[i][j + 1].lower() != txt[i][j]:
                    lst.append(t + [txt[i][last_point:j]])
                    last_point = j
                    t = []
            t.append(txt[i][last_point:])
        last_point = 0
        for j in range(1, len(txt[-1]) - 1):
            if txt[-1][j - 1] in '.!?' and txt[i][j] == ' ' and txt[-1][j + 1].lower() != txt[-1][j]:
                lst.append(t + [txt[-1][last_point:]])
                last_point = j
                t = []
        lst.append(t + [txt[-1][last_point:]])
        return lst

    remove_space(txt)
    lst = convert_text_to_sentences(txt)
    max_number = 0
    sent_with_max_number = 0
    for i in range(len(lst)):
        current_number = -1
        for el in lst[i]:
            current_number += el.count(' ') + 1
        if current_number > max_number:
            max_number = current_number
            sent_with_max_number = i
    for el in lst[sent_with_max_number]:
        print(el, end='')
    print()
    for i in range(len(txt)):
        for j in range(len(lst[sent_with_max_number])):
            txt[i] = txt[i].replace(lst[sent_with_max_number][j], '')
    txt.remove('')


commands = [('Напечатать текст', print_text),
            ('Выровнять по левому краю', left_alignment),
            ('Выровнять по правому краю', right_alignment),
            ('Выровнять по ширине', width_alignment),
            ('Удаление всех вхождений заданного слова', remove_word_from_text),
            ('Замена одного слова другим во всем тексте', replace_word_in_text),
            ('Вычисление арифметических выражений над целыми числами внутри текста', calculations),
            ('Найти (вывести на экран) и затем удалить Самое длинное по количеству слов предложение',
                find_and_remove_sentence),
            ('Завершить программу', exit)]


def print_menu():
    print()
    for i in range(len(commands)):
        print('{0}: {1}'.format(i + 1, commands[i][0]))


def input_command():
    while True:
        try:
            c = int(input('Введите команду: '))
            if c < 1 or c > 9:
                raise ValueError
            return c - 1
        except ValueError:
            print('Некорректная команда')


command = 0
count = 0
while True:
    if command == 0 or count > 5:
        print_menu()
        count = 0
    command = input_command()
    count += 1
    if command == 8:
        exit(0)
    else:
        commands[command][1](text)
