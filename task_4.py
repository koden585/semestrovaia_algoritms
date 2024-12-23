import time
import random
import matplotlib.pyplot as plt

# from semestrovaia.task_5 import selection_sort_dual


# Функция сортировки (обычная сортировка выбором)
def selection_sort(some_list):
    n = len(some_list)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if some_list[j] < some_list[min_idx]:
                min_idx = j
        if min_idx != i:
            some_list[i], some_list[min_idx] = some_list[min_idx], some_list[i]

# Функции генерации данных
def generate_random_list(n):
    return [random.randint(0, 1000) for _ in range(n)]

def generate_reversed_list(n):
    return list(range(n, 0, -1))

def generate_almost_sorted_list(n):
    lst = list(range(n))
    middle = n // 2
    if middle < n:
        lst[middle], lst[middle - 1] = lst[middle - 1], lst[middle]  # Один элемент не на месте
    return lst

def generate_half_zero_half_random(n):
    half_n = n // 2
    return [0] * half_n + [random.randint(1, 1000) for _ in range(n - half_n)]

def generate_near_sorted_list(n):
    lst = list(range(n))
    for i in range(n):
        swap_idx = random.randint(max(0, i - 10), min(n - 1, i + 10))
        lst[i], lst[swap_idx] = lst[swap_idx], lst[i]
    return lst

# Функция замера времени выполнения
def measure_time(sort_func, data):
    start = time.time()
    sort_func(data)
    return time.time() - start

# Размеры данных
sizes = [100, 500, 1000, 2000, 4000, 6000, 8000, 10000]
data_generators = {
    "Random": generate_random_list,
    "Reversed": generate_reversed_list,
    "Almost sorted": generate_almost_sorted_list,
    "Half zero, half random": generate_half_zero_half_random,
    "Near sorted": generate_near_sorted_list
}

# Проведение экспериментов
results = {dtype: [] for dtype in data_generators}

for size in sizes:
    print(f"Размер данных: {size}")
    for dtype, generator in data_generators.items():
        data = generator(size)
        time_taken = measure_time(selection_sort, data.copy())
        results[dtype].append(time_taken)
        print(f"  {dtype}: {time_taken:.4f} секунд")

plt.figure(figsize=(10, 6))

for dtype, times in results.items():
    plt.plot(sizes, times, label=dtype)

plt.title("Время выполнения сортировки выбором")
plt.xlabel("Размер данных (n)")
plt.ylabel("Время (секунды)")
plt.legend()
plt.grid()
plt.show()

"""
# Проведение экспериментов для двунаправленной сортировки 5 пункт
results_dual = {dtype: [] for dtype in data_generators}

for size in sizes:
    print(f"Размер данных: {size} (двунаправленная сортировка)")
    for dtype, generator in data_generators.items():
        data = generator(size)
        time_taken = measure_time(selection_sort_dual, data.copy())
        results_dual[dtype].append(time_taken)
        print(f"  {dtype}: {time_taken:.4f} секунд")

plt.figure(figsize=(10, 6))

for dtype, times in results_dual.items():
    plt.plot(sizes, times, label=dtype)

plt.title("Время выполнения двунаправленной сортировки выбором")
plt.xlabel("Размер данных (n)")
plt.ylabel("Время (секунды)")
plt.legend()
plt.grid()
plt.show()
"""