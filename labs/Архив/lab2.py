#  ИУ7-14Б Кривко Сергей
#Решение квадратного уравнения


#Ввод коэффициентов a, b, c
a = float(input('Введите коэффициент a: '))
b = float(input('Введите коэффициент b: '))
c = float(input('Введите коэффициент c: '))


if a == 0:
    if b == 0:
        if c == 0:
            #Если все коэффициенты равны 0, то х - любое действительное число
            print('x - любое число')
        else:
            #Если все коэффициенты, кроме с равны 0, то уравнение не имеет корней
            print('Корней нет')
    else:
        #Если a == 0, b != 0, c != 0, то уравнение обращается в линейное вида bx = -c
        x = -c / b
        print('x =', '{0:7g}'.format(x))
else:
    #Если a != 0, то считаем дискриминант
    D = b**2 - 4*a*c
    #Если дискриминант больше 0, то уравнение имеет два корня. Вычисляем их
    if D > 0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        print('x1 =', '{0:5g}'.format(x1))
        print('x2 =', '{0:5g}'.format(x2))
    #Если дискриминант равен 0, уравнение имеет 1 корень. Вычисляем его
    elif D == 0:
        x = -b / (2*a)
        print('x =', '{0:5g}'.format(x))
    #Если дискриминант меньше 0, уравнение не имеет корней
    else:
        print('Корней нет')

    
    
