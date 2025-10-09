"""
Задание 2 - Операции с матрицами
Функции для работы с 2D-матрицами: транспонирование, суммы по строкам и столбцам.
"""


def _is_rectangular(mat: list[list]) -> bool:
    if not mat:
        return True
    
    first_len = len(mat[0])
    return all(len(row) == first_len for row in mat)


def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    
    if not _is_rectangular(mat):
        raise ValueError("Матрица должна быть прямоугольной (все строки одной длины)")
    
    # Транспонирование через zip
    return [list(col) for col in zip(*mat)]


def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not _is_rectangular(mat):
        raise ValueError("Матрица должна быть прямоугольной (все строки одной длины)")
    
    return [sum(row) for row in mat]


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    
    if not _is_rectangular(mat):
        raise ValueError("Матрица должна быть прямоугольной (все строки одной длины)")
    
    # Используем транспонирование для получения столбцов
    return [sum(col) for col in zip(*mat)]


def print_matrix(mat: list[list], title: str = ""):

    if title:
        print(f"\n{title}:")
    if not mat:
        print("  []")
        return
    for row in mat:
        print(f"  {row}")


def main():
    
    print("ЗАДАНИЕ 2: Операции с матрицами")
    
    # Тест transpose
    print("\n1. Функция transpose(mat)")
    
    
    test_matrices = [
        [[1, 2, 3]],
        [[1], [2], [3]],
        [[1, 2], [3, 4]],
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        []
    ]
    
    for mat in test_matrices:
        print_matrix(mat, "Исходная матрица")
        result = transpose(mat)
        print_matrix(result, "Транспонированная")
        print()
    
    # Тест с рваной матрицей
    print("Тест с рваной матрицей:")
    try:
        transpose([[1, 2], [3]])
    except ValueError as e:
        print(f"  [[1, 2], [3]] → ValueError: {e}")
    
    # Тест row_sums
    print("\n2. Функция row_sums(mat)")
    
    
    test_matrices_sums = [
        [[1, 2, 3], [4, 5, 6]],
        [[-1, 1], [10, -10]],
        [[0, 0], [0, 0]],
        [[5], [10], [15]]
    ]
    
    for mat in test_matrices_sums:
        result = row_sums(mat)
        print(f"  {mat} → {result}")
    
    # Тест с рваной матрицей
    try:
        row_sums([[1, 2], [3]])
    except ValueError as e:
        print(f"  [[1, 2], [3]] → ValueError: {e}")
    
    # Тест col_sums
    print("\n3. Функция col_sums(mat)")
    
    
    for mat in test_matrices_sums:
        result = col_sums(mat)
        print(f"  {mat} → {result}")
    
    # Тест с рваной матрицей
    try:
        col_sums([[1, 2], [3]])
    except ValueError as e:
        print(f"  [[1, 2], [3]] → ValueError: {e}")
    
    


if __name__ == "__main__":
    main()

