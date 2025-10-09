"""
Задание 1 - Операции над списками
Функции для работы с массивами: поиск минимума/максимума, уникальные значения, flatten.
"""


def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:

    if not nums:
        raise ValueError("Список не может быть пустым")
    
    return (min(nums), max(nums))


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))


def flatten(mat: list[list | tuple]) -> list:
    result = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError(f"Ожидается список или кортеж, получен {type(row).__name__}")
        result.extend(row)
    return result


def main():
    print("ЗАДАНИЕ 1: Операции над списками")
    
    
    # Тест min_max
    print("\n1. Функция min_max(nums)")
    test_cases_minmax = [
        [3, -1, 5, 5, 0],
        [42],
        [-5, -2, -9],
        [1.5, 2, 2.0, -3.1]
    ]
    
    for nums in test_cases_minmax:
        result = min_max(nums)
        print(f"  {nums} → {result}")
    
    # Тест с пустым списком
    try:
        min_max([])
    except ValueError as e:
        print(f"  [] → ValueError: {e}")
    
    # Тест unique_sorted
    print("\n2. Функция unique_sorted(nums)")
    test_cases_unique = [
        [3, 1, 2, 1, 3],
        [],
        [-1, -1, 0, 2, 2],
        [1.0, 1, 2.5, 2.5, 0]
    ]
    
    for nums in test_cases_unique:
        result = unique_sorted(nums)
        print(f"  {nums} → {result}")
    
    # Тест flatten
    print("\n3. Функция flatten(mat)")
    test_cases_flatten = [
        [[1, 2], [3, 4]],
        [[1, 2], (3, 4, 5)],
        [[1], [], [2, 3]]
    ]
    
    for mat in test_cases_flatten:
        result = flatten(mat)
        print(f"  {mat} → {result}")
    
    # Тест с некорректным типом
    try:
        flatten([[1, 2], "ab"])
    except TypeError as e:
        print(f"  [[1, 2], \"ab\"] → TypeError: {e}")
    
    


if __name__ == "__main__":
    main()

