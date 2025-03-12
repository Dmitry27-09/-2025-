def check_fib(sequence):
    # Проверяем, что длина последовательности не менее 3 (минимальная длина для фибоначчиевой последовательности)
    if len(sequence) < 3:
        return False

    # Первые два элемента должны быть либо 0 и 1, либо 1 и 1
    if not ((sequence[0], sequence[1]) == (0, 1) or (sequence[0], sequence[1]) == (1, 1)):
        return False

    # Проверяем, что каждый следующий элемент равен сумме двух предыдущих
    for i in range(2, len(sequence)):
        if sequence[i] != sequence[i - 1] + sequence[i - 2]:
            return False

    return True


# Примеры тестов
print(check_fib([0, 1, 1, 2, 3, 5, 8]))  # Должно вернуть True
print(check_fib([1, 1, 2, 3, 5, 8, 13]))  # Должно вернуть True
print(check_fib([0, 1, 2, 3, 5, 8]))  # Должно вернуть False (неправильная последовательность)
print(check_fib([1, 2, 3, 5, 8]))  # Должно вернуть False (неправильная последовательность)
