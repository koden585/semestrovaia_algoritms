def selection_sort_dual(some_list):
    n = len(some_list)
    for i in range(n // 2):
        min_idx = i
        max_idx = i

        # Поиск минимального и максимального элементов в неотсортированной части
        for j in range(i + 1, n - i):
            if some_list[j] < some_list[min_idx]:
                min_idx = j
            if some_list[j] > some_list[max_idx]:
                max_idx = j

        # Перемещение минимального элемента в начало неотсортированной части
        if min_idx != i:
            some_list[i], some_list[min_idx] = some_list[min_idx], some_list[i]
            # Если максимальный элемент оказался на месте минимального, обновляем его индекс
            if max_idx == i:
                max_idx = min_idx

        # Перемещение максимального элемента в конец неотсортированной части
        if max_idx != n - i - 1:
            some_list[n - i - 1], some_list[max_idx] = some_list[max_idx], some_list[n - i - 1]

    return some_list

