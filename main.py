import random  # импортируем модуль random для генерации случайных чисел
# задаем список значений, из которых будет состоять матрица
values = [-15, -4, -2, -7, 0, 3, 5, 12, 9]
# генерируем случайное число для количества строк (высоты матрицы) от 4 до 8
height = random.randint(4, 8)
# генерируем случайное число для количества столбцов (ширины матрицы) от 4 до 8
width = random.randint(4, 8)
# создаем пустую матрицу
matrix = []
# наполняем матрицу значениями
for i in range(height):  # проходим по количеству строк
    row = []  # создаем новую строку
    for j in range(width):  # проходим по количеству столбцов
        # выбираем случайное значение из списка values и добавляем в строку
        row.append(random.choice(values))
    # добавляем строку в матрицу
    matrix.append(row)
# выводим матрицу в форматированном виде
for row in matrix:  # проходим по каждой строке матрицы
    print('\t'.join(map(str, row)))  # преобразуем значения в строки и выводим с табуляцией
def sum_3(matrix):
    total_sum = 0
    for row in matrix:
        for values in row:
            if values % 3 != 0:
                total_sum += values
    return total_sum
total_sum = sum_3(matrix)
text = "Сумма элементов, не кратных 3: "
print(f"{text}{total_sum}")
