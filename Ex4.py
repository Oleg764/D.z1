#  Указав номер четверти прямоугольной системы координат, 
# показать допустимые значения координат для точек этой четверти



quarter = int(input('Введите номер четверти (1-4)  '))
diapasones = ['(x > 0, y > 0)', '(x < 0, y > 0)', '(x < 0, y < 0)', '(x > 0, y < 0)']

def show_diapasone (quart, diapasones):
    return diapasones[quart-1]

print (f'{quarter}: {diapasones[quarter-1]}')