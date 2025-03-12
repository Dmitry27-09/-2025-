def max_subarray_sum(nums, k):
    # Проверка на недопустимые параметры
    if k <= 0 or k > len(nums):
        return 0  # Или можно поднять исключение

    # Инициализация максимальной суммы и суммы первого окна
    current_sum = sum(nums[:k])
    max_sum = current_sum

    # Обход оставшейся части массива
    for i in range(len(nums) - k):
        # Вычисление новой суммы окна
        current_sum = current_sum - nums[i] + nums[i + k]
        # Обновление максимальной суммы
        max_sum = max(max_sum, current_sum)

    return max_sum

# Тестирование функции
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result = max_subarray_sum(nums, k)
print(result)

