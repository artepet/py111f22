"""2.	Считалочка
Дано N человек, считалка из K слогов.
Считалка начинает считать с первого человека.
Когда считалка досчитывает до k-го слога, человек, на котором она остановилась, вылетает.
Игра происходит до тех пор, пока не останется последний человек.
Для данных N и К дать номер последнего оставшегося человека."""
def schitalochka(n, k):
    if n == 1:
        return 0
    else:
        return (schitalochka(n-1, k) + k) % n

n = int(input())
k = int(input())
last_person = schitalochka(n, k) + 1  # добавляем 1, чтобы нумерация начиналась с 1
print(f"Последний оставшийся человек: {last_person}")


"""4.	Навигатор на сетке.
Дана плоская квадратная двумерная сетка (массив), на которой определена стоимость захода в каждую ячейку  (все стоимости положительные). 
Необходимо найти путь минимальной стоимости из заданной ячейки в заданную ячейку и вывести этот путь."""
import heapq

def dijkstra(grid, start, end):
    m = len(grid)
    n = len(grid[0])

    # Инициализация стоимости и посещенных ячеек
    costs = [[float('inf')] * n for _ in range(m)]
    costs[start[0]][start[1]] = grid[start[0]][start[1]]
    visited = [[False] * n for _ in range(m)]

    # Инициализация пути
    paths = {(i, j): [] for j in range(n) for i in range(m)}
    paths[start] = [start]

    # Очередь с приоритетом для хранения ячеек
    q = []
    heapq.heappush(q, (costs[start[0]][start[1]], start))

    while q:
        # Извлечение ячейки с минимальной стоимостью
        _, curr = heapq.heappop(q)

        # Проверка, является ли ячейка конечной
        if curr == end:
            return paths[curr]

        # Перебор соседних ячеек
        row, col = curr
        for i, j in [(row-1,col), (row+1,col), (row,col-1), (row,col+1)]:
            if 0 <= i < m and 0 <= j < n and not visited[i][j]:
                # Обновление стоимости и пути
                new_cost = costs[row][col] + grid[i][j]
                if new_cost < costs[i][j]:
                    costs[i][j] = new_cost
                    paths[(i, j)] = paths[(row, col)] + [(i, j)]
                    heapq.heappush(q, (new_cost, (i, j)))

        # Пометка текущей ячейки как посещенной
        visited[row][col] = True

    # Если не найдено пути до конечной ячейки, вернуть None
    return None

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
start = (0, 0)
end = (2, 2)
path = dijkstra(grid, start, end)
print(path)


"""6.	Аренда ракет
Вы – компания, дающая в аренду ракеты. Каждый день к вам приходит список заявок на использование ракет в виде: (час_начала, час_конца), (час_начала, час_конца), ...
Если аренда ракеты заканчивается в час X, то в этот же час ее уже можно взять в аренду снова (т.е. час_начала может начинаться с Х).
Дано: список заявок на использование ракет
Задача: вывести ответ, хватит ли вам одной ракеты, чтобы удовлетворить все заявки на этот день"""
def can_satisfy_all_requests(requests):
    """
Функция принимает на вход список заявок requests,
где каждая заявка представлена в виде (час_начала, час_конца).
Внутри функции происходит сортировка заявок по времени начала аренды, после чего проходится
по каждой заявке и проверяется наличие пересечения между ее временным интервалом и временными
интервалами предыдущих заявок. Если такое пересечение есть, функция возвращает False.
Если же такого пересечения нет, функция возвращает True.
    :param requests:
    :return:
    """
    requests.sort() # Сортировка заявок по времени начала аренды
    end_time = 0 # Время, когда закончится аренда предыдущей заявки
    for request in requests:
        if request[0] < end_time: # Проверка на пересечение временных интервалов
            return False
        end_time = request[1]
    return True


"""7.	Сорт
Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
Задача: отсортировать массив наиболее эффективным способом"""

import random
# сортировки слиянием
def merge_sort(array):
    if len(array) <= 1:
        return array
    # Разделение пополам
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    # Рекурсивная сортировка половин
    left = merge_sort(left)
    right = merge_sort(right)
    # Слияние
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

# Создание массива из 10**6 целых чисел на отрезке [13, 25]
array = [random.randint(13, 25) for _ in range(10**6)]
# Сортировка
sorted_array = merge_sort(array)

print(sorted_array)