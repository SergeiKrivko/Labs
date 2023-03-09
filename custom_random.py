import random


f = open('CustomRandom\\EnglishSurnames.txt')
english_surnames = []
for line in f:
    english_surnames.append(line.strip())

f = open('CustomRandom\\EnglishNames.txt')
english_names = []
for line in f:
    english_names.append(line.strip())

f = open('CustomRandom\\RussianSurnames.txt')
russian_surnames = []
for line in f:
    russian_surnames.append(line.strip())

f = open('CustomRandom\\RussianFemaleNames.txt')
russian_female_names = []
for line in f:
    russian_female_names.append(line.strip())

f = open('CustomRandom\\RussianMaleNames.txt')
russian_male_names = []
for line in f:
    russian_male_names.append(line.strip())


def translite(st):
    alph = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sh', 'ь': '', 'ы': 'i', 'ъ': '',
            'э': 'e', 'ю': 'yu', 'я': 'ya'}
    res = ''
    for symbol in st:
        if symbol in alph:
            res += alph[symbol]
        elif symbol.lower() in alph:
            res += alph[symbol.lower()].upper()
        else:
            res += symbol
    return res


def random_surname(language='english', female=False):
    if language == 'english':
        return english_surnames[random.randint(0, len(english_surnames) - 1)]
    if language == 'russian':
        if female:
            surname = russian_surnames[random.randint(0, len(russian_surnames) - 1)]
            if surname[-2:] in 'ов,ев,ин,ын':
                surname += 'а'
            elif surname[-2:] in 'ий,ый':
                surname = surname[:-2] + 'ая'
            return surname
        return russian_surnames[random.randint(0, len(russian_surnames) - 1)]


def random_name(language='english', female=False):
    if language == 'english':
        return english_names[random.randint(0, len(english_names) - 1)]
    if language == 'russian':
        if female:
            return russian_female_names[random.randint(0, len(russian_female_names) - 1)]
        return russian_male_names[random.randint(0, len(russian_male_names) - 1)]
