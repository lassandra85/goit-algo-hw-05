def binary_search(arr_data, target_value):
    left, right = 0, len(arr_data) - 1  # Ініціалізація меж пошуку: лівий і правий індекси
    iterations_count = 0  # Лічильник кількості ітерацій
    upper_bound_index = None  # Змінна для збереження верхньої межі, яка більша за target_value

    while left <= right:  # Поки лівий індекс не перевищує правий
        iterations_count += 1  # Збільшуємо кількість ітерацій
        mid = (left + right) // 2  # Знаходимо середній індекс

        if arr_data[mid] == target_value:  # Якщо елемент на середньому індексі є шуканим
            return (iterations_count, arr_data[mid])  # Повертаємо кількість ітерацій та знайдений елемент
        elif arr_data[mid] < target_value:  # Якщо середній елемент менший за шуканий
            left = mid + 1  # Переміщаємо ліву межу правіше
        else:  # Якщо середній елемент більший за шуканий
            right = mid - 1  # Переміщаємо праву межу лівіше

    # Якщо шуканий елемент не знайдений, шукаємо верхню межу
    if left < len(arr_data):  # Якщо залишок правої частини непорожній
        upper_bound_index = arr_data[left]  # Верхня межа — перший елемент, більший за target_value
    else:  # Якщо верхньої межі не знайдено
        upper_bound_index = "Не знайдена верхня межа"  # Повертаємо повідомлення про відсутність верхньої межі

    return (iterations, upper_bound_index)  # Повертаємо кількість ітерацій та верхню межу


# Приклад 1:
arr = [12.5, 13.7, 18.2, 25.6, 50.1, 70.8]
target = 18.2
iterations, upper_bound = binary_search(arr, target)
print(f"Ітерацій: {iterations}, Верхня межа: {upper_bound}")

# Приклад 2:
arr = [100.5, 150.2, 200.3, 250.4, 300.6]
target = 210.0
iterations, upper_bound = binary_search(arr, target)
print(f"Ітерацій: {iterations}, Верхня межа: {upper_bound}")

# Приклад 3:
arr = [1.1, 5.5, 10.0, 20.3, 50.8]
target = 7.5
iterations, upper_bound = binary_search(arr, target)
print(f"Ітерацій: {iterations}, Верхня межа: {upper_bound}")