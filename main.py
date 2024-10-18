import random  # Импортируем библиотеку random для генерации случайных чисел
# Список значений для заполнения матрицы
values = [-15, -4, -2, -7, 0, 3, 5, 12, 9]
# Генерируем случайные размеры матрицы от 4 до 8
height = random.randint(4, 8)  # Высота матрицы
width = random.randint(4, 8)   # Ширина матрицы
# Создаем пустую матрицу заданного размера
matrix = [[0] * width for _ in range(height)]  # Заполняем её нулями
# Заполняем матрицу случайными значениями из списка
for i in range(height):  # Цикл по строкам
    for j in range(width):  # Цикл по столбцам
        matrix[i][j] = random.choice(values)  # Случайно выбираем значение из списка
# Выводим матрицу в форматированном виде
print("Матрица:")
for row in matrix:  # Цикл по строкам матрицы
    print(" | ".join(f"{num:3}" for num in row))  # Форматированный вывод строки
# Считаем сумму элементов матрицы, некратных 3
sum_not_divisible_by_3 = sum(num for row in matrix for num in row if num % 3 != 0)
# Выводим сумму
print(f"Сумма всех элементов, некратных 3: {sum_not_divisible_by_3}")
