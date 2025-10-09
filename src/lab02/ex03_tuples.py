"""
Задание 3 - Работа с кортежами
Форматирование записей студентов в виде кортежей (ФИО, группа, GPA).
"""


def format_record(rec: tuple[str, str, float]) -> str:
    
    # Проверка, что на вход поступает именно tuple
    if not isinstance(rec, tuple):
        raise TypeError(f"Ожидается tuple, получен {type(rec).__name__}")
    
    # Проверка, что в tuple ровно 3 элемента
    if len(rec) != 3:
        raise ValueError(f"Ожидается ровно 3 элемента, получено {len(rec)}")
    
    fio, group, gpa = rec
    
    # Проверка типов
    if not isinstance(fio, str):
        raise TypeError("ФИО должно быть строкой")
    if not isinstance(group, str):
        raise TypeError("Группа должна быть строкой")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должен быть числом")
    
    # Очистка и нормализация ФИО
    # Убираем лишние пробелы и разбиваем на части
    fio_parts = fio.strip().split()
    fio_parts = [part for part in fio_parts if part]  # Удаляем пустые части
    
    if not fio_parts:
        raise ValueError("ФИО не может быть пустым")
    
    # Нормализуем регистр (первая буква заглавная, остальные строчные)
    fio_parts = [part.capitalize() for part in fio_parts]
    
    # Формируем фамилию и инициалы
    if len(fio_parts) < 1:
        raise ValueError("ФИО должно содержать хотя бы фамилию")
    
    surname = fio_parts[0]
    
    # Формируем инициалы из имени и отчества (если есть)
    initials = []
    for i in range(1, len(fio_parts)):
        if fio_parts[i]:
            initials.append(fio_parts[i][0].upper() + ".")
    
    # Формируем строку с инициалами
    if initials:
        formatted_fio = f"{surname} {''.join(initials)}"
    else:
        formatted_fio = surname
    
    # Проверка группы
    group = group.strip()
    if not group:
        raise ValueError("Группа не может быть пустой")
    
    # Форматируем строку
    formatted_str = f"{formatted_fio}, гр. {group}, GPA {gpa:.2f}"
    
    return formatted_str


def main():
    
    print("ЗАДАНИЕ 3: Форматирование записей студентов")
    
    
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
    
    # Тесты на ошибки
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
    
    


if __name__ == "__main__":
    main()

