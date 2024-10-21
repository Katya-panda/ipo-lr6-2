import random  # импортируем библиотеку random для генерации случайных чисел
# список значений для заполнения матрицы
values = [-15, -4, -2, -7, 0, 3, 5, 12, 9]
# генерируем случайные размеры матрицы от 4 до 8
height = random.randint(4, 8)  # высота матрицы
width = random.randint(4, 8)   # щирина матрицы
# создаем пустую матрицу заданного размера
matrix = [[0] * width for _ in range(height)]  # заполняем её нулями
# заполняем матрицу случайными значениями из списка
for i in range(height):  # цикл по строкам
    for j in range(width):  # цикл по столбцам
        matrix[i][j] = random.choice(values)  # случайно выбираем значение из списка
# выводим матрицу в форматированном виде
print("Матрица:")
for row in matrix:  # цикл по строкам матрицы
    print(" | ".join(f"{num:3}" for num in row))  # форматированный вывод строки
# считаем сумму элементов матрицы, некратных 3
sum_not_divisible_by_3 = sum(num for row in matrix for num in row if num % 3 != 0)
# выводим сумму
print(f"Сумма всех элементов, некратных 3: {sum_not_divisible_by_3}")
