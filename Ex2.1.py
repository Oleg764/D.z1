# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = int(input('Введите значение x   (0 - no, 1 - yes)  = '))
y = int(input('Введите значение y   (0 - no, 1 - yes)  = '))
z = int(input('Введите значение z  (0 - no, 1 - yes)  = '))
left = not (x or y or z)
right = not x and not y and not z
statement_right = left == right

print(statement_right)
