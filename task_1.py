def selection_sort(some_list):
    n = len(some_list)  # Определяем длину списка

    comparisons = 0  # Количество сравнений
    swaps = 0  # Количество перестановок

    print("Исходный список:", some_list)

    # Основной цикл по элементам списка
    for i in range(n):
        min_idx = i  # Считаем, что текущий элемент - минимальный

        # Вложенный цикл для поиска минимального элемента в оставшейся части списка
        for j in range(i + 1, n):
            comparisons += 1  # Увеличиваем количество сравнений

            # Если найден элемент меньше текущего минимального, обновляем индекс
            if some_list[j] < some_list[min_idx]:
                min_idx = j

        # Если минимальный элемент не равен текущему, выполняем перестановку
        if min_idx != i:
            # Меняем местами текущий элемент и минимальный
            some_list[i], some_list[min_idx] = some_list[min_idx], some_list[i]
            swaps += 1  # Увеличиваем счетчик перестановок
        print(f"Итерация {i + 1}: {some_list}")

    print(f"Итоговый список: {some_list}")  # Выводим итоговый список после сортировки
    print(f"Всего сравнений: {comparisons}, всего перестановок: {swaps}")


data1 = [7, 3, 9, 4, 2, 5, 6, 1, 8]
selection_sort(data1)
