"""
Задание 3 - Работа с кортежами
Форматирование записей студентов в виде кортежей (ФИО, группа, GPA).
"""


def validate_record_structure(rec) -> None:
    """
    Проверяет структуру записи (тип и количество элементов).
    
    Args:
        rec: Запись для проверки
        
    Raises:
        TypeError: Если rec не является tuple
        ValueError: Если количество элементов не равно 3
    """
    if not isinstance(rec, tuple):
        raise TypeError(f"Ожидается tuple, получен {type(rec).__name__}")
    
    if len(rec) != 3:
        raise ValueError(f"Ожидается ровно 3 элемента, получено {len(rec)}")


def validate_field_types(fio: str, group: str, gpa: float) -> None:
    """
    Проверяет типы полей записи.
    
    Args:
        fio: ФИО студента
        group: Группа студента
        gpa: GPA студента
        
    Raises:
        TypeError: Если типы полей не соответствуют ожидаемым
    """
    if not isinstance(fio, str):
        raise TypeError("ФИО должно быть строкой")
    if not isinstance(group, str):
        raise TypeError("Группа должна быть строкой")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должен быть числом")


def parse_fio_parts(fio: str) -> list[str]:
    """
    Разбивает ФИО на части и нормализует регистр.
    
    Args:
        fio: Строка с ФИО
        
    Returns:
        Список нормализованных частей ФИО
        
    Raises:
        ValueError: Если ФИО пустое
    """
    fio_parts = fio.strip().split()
    fio_parts = [part for part in fio_parts if part]
    
    if not fio_parts:
        raise ValueError("ФИО не может быть пустым")
    
    return [part.capitalize() for part in fio_parts]


def format_fio_with_initials(fio_parts: list[str]) -> str:
    """
    Форматирует ФИО в формат "Фамилия И.О."
    
    Args:
        fio_parts: Список частей ФИО (фамилия, имя, отчество)
        
    Returns:
        Отформатированная строка ФИО
    """
    surname = fio_parts[0]
    
    # Формируем инициалы из имени и отчества
    initials = [part[0].upper() + "." for part in fio_parts[1:] if part]
    
    if initials:
        return f"{surname} {''.join(initials)}"
    return surname


def normalize_fio(fio: str) -> str:
    """
    Нормализует и форматирует ФИО студента.
    
    Args:
        fio: Строка с ФИО
        
    Returns:
        Отформатированная строка ФИО в формате "Фамилия И.О."
        
    Raises:
        ValueError: Если ФИО некорректно
    """
    fio_parts = parse_fio_parts(fio)
    return format_fio_with_initials(fio_parts)


def validate_group(group: str) -> str:
    """
    Проверяет и нормализует название группы.
    
    Args:
        group: Название группы
        
    Returns:
        Нормализованное название группы
        
    Raises:
        ValueError: Если группа пустая
    """
    group = group.strip()
    if not group:
        raise ValueError("Группа не может быть пустой")
    return group


def format_record(rec: tuple[str, str, float]) -> str:
    """
    Форматирует запись о студенте в строку.
    
    Args:
        rec: Кортеж из трёх элементов (ФИО, группа, GPA)
        
    Returns:
        Отформатированная строка вида "Фамилия И.О., гр. Группа, GPA X.XX"
        
    Raises:
        TypeError: Если rec не tuple или типы полей некорректны
        ValueError: Если структура или значения полей некорректны
    """
    validate_record_structure(rec)
    
    fio, group, gpa = rec
    
    validate_field_types(fio, group, gpa)
    
    formatted_fio = normalize_fio(fio)
    validated_group = validate_group(group)
    
    return f"{formatted_fio}, гр. {validated_group}, GPA {gpa:.2f}"


def run_success_tests() -> None:
    """Выполняет тесты с корректными данными."""
    print("\nФункция format_record(rec)")
    
    test_cases = [
        ("Иванов Иван Иванович", "BIVT-25", 4.6),
        ("Петров Пётр", "IKBO-12", 5.0),
        ("Петров Пётр Петрович", "IKBO-12", 5.0),
        ("  сидорова  анна   сергеевна ", "ABB-01", 3.999),
        ("Смирнов Алексей", "БИВТ-22", 4.5),
        ("Козлова Мария Владимировна", "ИКБО-15", 4.87),
    ]
    
    for rec in test_cases:
        result = format_record(rec)
        print(f"\nВход: {rec}")
        print(f"Результат: {result}")


def run_error_tests() -> None:
    """Выполняет тесты на обработку ошибок."""
    print("\n\nТесты на обработку ошибок:")
    
    error_cases = [
        (["Иванов Иван", "BIVT-25", 4.5], "Список вместо tuple"),
        (("Иванов Иван", "BIVT-25"), "Только 2 элемента"),
        (("Иванов Иван", "BIVT-25", 4.5, "лишний"), "4 элемента вместо 3"),
        (("", "BIVT-25", 4.5), "Пустое ФИО"),
        (("Иванов Иван", "", 4.5), "Пустая группа"),
        (("Иванов Иван", "BIVT-25", "не число"), "GPA не число"),
    ]
    
    for rec, description in error_cases:
        try:
            format_record(rec)
        except (ValueError, TypeError) as e:
            print(f"\n{description}:")
            print(f"  Вход: {rec}")
            print(f"  Ошибка: {type(e).__name__}: {e}")


def main():
    """Главная функция для запуска всех тестов."""
    print("ЗАДАНИЕ 3: Форматирование записей студентов")
    
    run_success_tests()
    run_error_tests()


if __name__ == "__main__":
    main()
