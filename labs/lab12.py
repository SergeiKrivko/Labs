#   Кривко Сергей ИУ7-14Б
# Текстовый процессор


text = ['Отец мой Андрей Петрович Гринев в молодости своей служил при графе Минихе',
        'и вышел в отставку премьер-майором в 1800 - 61 + 5 году. С тех пор жил он в своей',
        'Симбирской деревне, где и женился на девице Авдотье Васильевне ***, дочери',
        'бедного тамошнего дворянина. Нас было девять человек детей. Все мои братья',
        'и сестры умерли во младенчестве. Матушка была еще мною брюхата, как уже я',
        'был записан в Семеновский полк сержантом, по милости майора гвардии князя ***,',
        'близкого нашего родственника. Если бы паче всякого чаяния матушка родила дочь,',
        'то батюшка объявил бы куда следовало о смерти неявившегося сержанта, и дело',
        'тем бы и кончилось. Я считался в отпуску до окончания наук. В то время',
        'воспитывались мы не по-нонешнему. С пятилетнего возраста отдан я был на',
        'руки стремянному Савельичу, за трезвое поведение пожалованному мне в',
        'дядьки. Под его надзором на двенадцатом году выучился я русской грамоте',
        'и мог очень здраво судить о свойствах борзого кобеля. В это время батюшка',
        'нанял для меня француза, мосье Бопре, которого выписали из Москвы вместе с',
        'годовым запасом вина и прованского масла. Приезд его сильно не понравился',
        'Савельичу.']


def print_text(txt):
    """Вывод текста на экран"""
    if len(txt) == 0:
        print('\nТекст закончился\n')
    else:
        print()
        for st in txt:
            print(st)


def left_alignment(txt):
    """Вырвнивание текста по левому краю"""
    remove_extra_spaces(txt)


def right_alignment(txt):
    """Выравнивание текста по правому краю"""
    max_len = 0     # Максимальная длина строки
    remove_extra_spaces(txt)
    for i in range(len(txt)):
        max_len = max(max_len, len(txt[i]))
    for i in range(len(txt)):
        txt[i] = '{0:>{1}}'.format(txt[i], max_len)


def width_alignment(txt):
    """Выравнивание текста по ширине"""
    max_len = 0     # Максимальная длина строки
    remove_extra_spaces(txt)
    for i in range(len(txt)):
        max_len = max(max_len, len(txt[i]))
    for i in range(len(txt)):
        # lst = txt[i].split()
        # old_count = len(lst) - 1        # Старое кол-во пробелов в строке
        # if old_count:
        #     new_count = max_len - len(txt[i])       # Кол-во пробелов, которое необходимо добавить
        #     s = ''
        #     for j in range(len(lst)):
        #         if new_count % old_count > j:
        #             s += lst[j] + ' ' * (2 + new_count // old_count)
        #         else:
        #             s += lst[j] + ' ' * (1 + new_count // old_count)
        #     txt[i] = s
        # else:
        #     txt[i] = '{0:<{1}}'.format(txt[i], max_len)
        old_count = txt[i].count(' ')
        if old_count:
            new_count = max_len - len(txt[i])
            txt[i] = txt[i].replace(' ', ' ' * (new_count // old_count + 1))
            txt[i] = txt[i].replace(' ' * (new_count // old_count + 1), ' ' * (new_count // old_count + 2), new_count
                                    % old_count)
        else:
            txt[i] = '{0:<{1}}'.format(txt[i], max_len)


def remove_extra_spaces(txt):
    """Удаление лишних пробелов из текста"""
    for i in range(len(txt)):
        # txt[i] = ' '.join(txt[i].split())
        while '  ' in txt[i]:
            txt[i] = txt[i].replace('  ', ' ')
        txt[i] = txt[i].strip()


def remove_word(txt, word):
    """Удаление слова из текста"""
    for i in range(len(txt)):
        txt[i] = ' ' + txt[i] + ' '
        for symbol in ' .,:;!?':
            txt[i] = txt[i].replace(' ' + word + symbol, symbol)
        txt[i] = txt[i].strip()


def remove_word_from_text(txt):
    """Ввод слова и его удаление из текста"""
    word = input('Введите слово для удаления: ')
    remove_word(txt, word)


def replace_word(txt, word1, word2):
    """Замена word1 на word2 во всем тексте"""
    for i in range(len(txt)):
        txt[i] = ' ' + txt[i] + ' '
        for symbol in ' .,:;':
            txt[i] = txt[i].replace(' ' + word1 + symbol, ' ' + word2 + symbol)
        txt[i] = txt[i].strip()


def replace_word_in_text(txt):
    """Ввод двух слов и замена одного другим во всем тексте"""
    word1 = input('Введите заменяемое слово: ')
    word2 = input('Введите новое слово: ')
    replace_word(txt, word1, word2)


def calculations(txt):
    """Вычисление арифметических выражений в тексте"""
    a = []
    for j in range(len(txt)):
        a.append(txt[j].split())
    for j in range(len(txt)):           # Проходим по всем строкам
        i = 0
        while i < len(a[j]) - 2:           # Ищем знаки '+' и '-'
            if a[j][i] == '+':
                try:                    # Если нашли, пытаемся преобразовать то, что стоит справа и слева к числу и
                    a[j][i] = str(int(a[j][i - 1]) + int(a[j][i + 1]))           # сложить/вычесть
                    a[j].pop(i + 1)
                    a[j].pop(i - 1)
                except ValueError:
                    i += 1
            elif a[j][i] == '-':
                try:
                    a[j][i] = str(int(a[j][i - 1]) - int(a[j][i + 1]))
                    a[j].pop(i + 1)
                    a[j].pop(i - 1)
                except ValueError:
                    i += 1
            else:
                i += 1
        i += 1
        if j < len(txt) - 1:
            # Рассматриваем последнее слово строки
            if a[j][i] == '+':
                try:  # Если это '+' или '-', пытаемся преобразовать то, что стоит слева и на след строке к числу и
                    a[j][i] = str(int(a[j][i - 1]) + int(a[j + 1][0]))  # сложить/вычесть
                    a[j + 1].pop(0)
                    a[j].pop(i - 1)
                except ValueError:
                    pass
            elif a[j][i] == '-':
                try:
                    a[j][i] = str(int(a[j][i - 1]) - int(a[j + 1][0]))
                    a[j].pop(0)
                    a[j].pop(i - 1)
                except ValueError:
                    pass
        # Склеиваем список обратно в строку
        txt[j] = ''
        for el in a[j]:
            txt[j] += el + ' '


def find_and_remove_sentence(txt):
    """Поиск и удаление самого длинного предложения из текста"""
    def convert_text_to_sentences(txt):
        """Преобразование текста в список предложений"""
        lst = []
        t = []          # Остаток строки
        for i in range(len(txt) - 1):
            last_point = 0          # Конец предыдущего предложения
            for j in range(len(txt[i])):     # Проходим по всем символам строки и ищем концы предложений
                if txt[i][j] in '.!?':
                    lst.append(t + [txt[i][last_point:j + 1]])      # Добавляем предложение в список
                    last_point = j + 1
                    t = []
            t.append(txt[i][last_point:])           # Добавляем остаток строки в переменную t
        last_point = 0
        for j in range(1, len(txt[-1]) - 1):    # Проходим по всем символам последней строки и ищем концы предложений
            if txt[-1][j - 1] in '.!?' and txt[-1][j] == ' ' and txt[-1][j + 1].lower() != txt[-1][j]:
                lst.append(t + [txt[-1][last_point:]])      # Добавляем предложение в список
                last_point = j
                t = []
        lst.append(t + [txt[-1][last_point:]])
        return lst

    if len(txt) == 0:
        return
    remove_extra_spaces(txt)
    sentences = convert_text_to_sentences(txt)
    max_number = 0          # Наибольшее число слов в предложении
    sent_with_max_number = 0        # Номер предложения с наибольшим кол-вом слов
    for i in range(len(sentences)):
        current_number = -1     # Кол-во слов в текущем предложении
        for el in sentences[i]:
            current_number += el.count(' ') + 1
        if current_number > max_number:         # Обновление максимумов
            max_number = current_number
            sent_with_max_number = i
    for el in sentences[sent_with_max_number]:        # Вывод самого длинного предложения
        print(el, end=' ')
    print()
    for i in range(len(txt)):                   # Удаление предложения
        for sentence_part in sentences[sent_with_max_number]:
            txt[i] = txt[i].replace(sentence_part, '')
    for i in range(len(txt)):
        txt[i] = txt[i].strip()
    while '' in txt:
        txt.remove('')


def command_exit(*args):
    exit(0)


# Список доступных команд
commands = [('Напечатать текст', print_text),
            ('Выровнять по левому краю', left_alignment),
            ('Выровнять по правому краю', right_alignment),
            ('Выровнять по ширине', width_alignment),
            ('Удаление слова', remove_word_from_text),
            ('Замена слова', replace_word_in_text),
            ('Вычисление арифметических выражений', calculations),
            ('Найти и удалить самое длинное предложение',
                find_and_remove_sentence),
            ('Завершить программу', command_exit)]


def print_menu(commands):
    """Вывод списка команд на экран"""
    print()
    for i in range(len(commands)):
        print('{0}: {1}'.format(i + 1, commands[i][0]))


def input_command(commands):
    """Ввод команды"""
    while True:
        try:
            c = int(input('Введите команду: '))
            if c < 1 or c > len(commands):
                raise ValueError
            return c - 1
        except ValueError:
            print('Некорректная команда')


command = 0     # Текущая команда
print_text(text)
while True:
    print_menu(commands)
    command = input_command(commands)
    commands[command][1](text)          # Вызов команды
    if command != 1:
        print_text(text)
