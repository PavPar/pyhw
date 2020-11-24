# 1. Нарисовать рамочку шириной w символов и
# высотой h символов.
def draw(w, h):
    symbol = '*'
    base = ' ' * w
    base = list(base)
    base[0] = symbol
    base[-1] = symbol
    base = ''.join(base)
    rect = [base for _ in range(0, h + 1)]
    rect[0] = symbol * w
    rect[-1] = symbol * w
    return rect


# 2. Пускай символ, которым рисуется рамочка –
# тоже входной параметр.

def draw_2(w, h, symbol):
    base = ' ' * (w)
    base = list(base)
    base[0] = symbol
    base[-1] = symbol
    base = ''.join(base)
    rect = [base for _ in range(0, h + 1)]
    rect[0] = symbol * w
    rect[-1] = symbol * w
    return rect


# 3. Нарисовать рамочку шириной w символов и
# высотой h символов, и толщиной f символов.
# (оформить в виде функции)

def draw_3(w, h, f, symbol):
    base = ' ' * (w)
    base = list(base)
    for i in range(0, w):
        if i < f or i > w - f - 1:
            base[i] = symbol
    base = ''.join(base)
    rect = [base for _ in range(0, h + 1)]
    for i in range(0, h + 1):
        if i < f or i > h - f:
            rect[i] = symbol * w
    return rect


print('Задание 1')
res = draw(10, 5)
for i in res:
    print(i)

print('Задание 2')
res = draw_2(10, 5, '#')
for i in res:
    print(i)

print('Задание 3')
res = draw_3(100, 50, 10, '#')
for i in res:
    print(i)
