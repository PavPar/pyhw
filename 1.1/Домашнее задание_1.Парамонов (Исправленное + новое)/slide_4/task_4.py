# -*- coding: utf-8 -*-
print(' Вариант №' + str(len('ПарамоновПавелАлександрович') % 4 + 1))


# Вариант №4
#
# Создайте приложение, которое проверяет правильность номера введенной кредитной карты (см.
# алгоритм Луна)
#
# Оригинальный алгоритм, описанный разработчиком

# 1. Цифры проверяемой последовательности нумеруются справа налево.
# 2. Цифры, оказавшиеся на нечётных местах, остаются без изменений.
# 3. Цифры, стоящие на чётных местах, умножаются на 2.
# 4. Если в результате такого умножения возникает число больше 9, оно заменяется суммой цифр
# получившегося произведения — однозначным числом, то есть цифрой.
# 5. Все полученные в результате преобразования цифры складываются. Если сумма кратна 10,
# то исходные данные верны.

def toDict(inptList):
    return {i: int(inptList[i]) for i in range(0, len(inptList))}


def luhn(creditNum):
    digits = list(creditNum)
    digits.reverse()
    try:
        digitsDict = toDict(digits)
    except:
        print('->Ошибка данных. Повторите ввод')
        return False

    for i in range(0, len(digitsDict), 2):
        digitsDict[i] *= 2
        if digitsDict[i] > 9:
            digitsDict[i] = (digitsDict[i] // 10) + (digitsDict[i] % 10)
    return sum(digitsDict.values()) % 10 == 0


def validate(creditNum):
    if (luhn(creditNum)):
        print('-> Номер кредитной карты правильный', '\n')
    else:
        print('-> Неправильный номер карты', '\n')


def app():
    while (True):
        print('Введите данные карты')
        print('или exit для выхода из приложения')
        print('=' * 50)
        data = input()
        if data == 'exit':
            break;
        validate(data)


app()
