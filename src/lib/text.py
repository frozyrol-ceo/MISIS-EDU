import re
from typing import Dict, List, Tuple, Set

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    result = text

    # Замена ё/Ё на е/Е
    if yo2e:
        result = result.replace('ё', 'е').replace('Ё', 'Е')

    # Приведение к нижнему регистру
    if casefold:
        result = result.casefold()

    # Замена управляющих символов на пробелы
    result = result.replace('\t', ' ').replace('\r', ' ').replace('\n', ' ')

    # Схлопывание последовательностей пробелов в один
    result = re.sub(r'\s+', ' ', result)

    # Обрезка пробелов с краёв
    result = result.strip()

    return result


def tokenize(text: str) -> List[str]:
    # Шаблон: последовательность \w, допускающая дефисы внутри
    pattern = r'\w+(?:-\w+)*'
    tokens = re.findall(pattern, text)
    return tokens


def count_freq(tokens: List[str]) -> Dict[str, int]:
    freq: Dict[str, int] = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq


def top_n(freq: Dict[str, int], n: int = 5) -> List[Tuple[str, int]]:
    # Сортируем по ключу: (-частота, слово)
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]


def print_test_cases():
    #Выводит все тест-кейсы для функций normalize, tokenize, count_freq + top_n
    
    print("ТЕСТ-КЕЙСЫ ДЛЯ ФУНКЦИЙ ОБРАБОТКИ ТЕКСТА")
    
    
    # Тест-кейсы для normalize
    print("\n1. ФУНКЦИЯ normalize:")
    
    
    test_cases_normalize = [
        ('"ПрИвЕт\\nМИр\\t"', 'normalize("ПрИвЕт\\nМИр\\t")', '"привет мир"', '(casefold + схлопнуть пробелы)'),
        ('"ёжик, Ёлка"', 'normalize("ёжик, Ёлка")', '"ежик, елка"', '(yo2e=True)'),
        ('"Hello\\r\\nWorld"', 'normalize("Hello\\r\\nWorld")', '"hello world"', ''),
        ('"  двойные   пробелы  "', 'normalize("  двойные   пробелы  ")', '"двойные пробелы"', '')
    ]
    
    for input_desc, func_call, expected, comment in test_cases_normalize:
        print(f"• Вход: {input_desc}")
        print(f"  Вызов: {func_call}")
        print(f"  Ожидаемый результат: {expected}")
        if comment:
            print(f"  Комментарий: {comment}")
        print()
    
    # Тест-кейсы для tokenize
    print("\n2. ФУНКЦИЯ tokenize:")
    print("-" * 40)
    print("(предполагаем, что текст уже normalize)")
    print()
    
    test_cases_tokenize = [
        ('"привет мир"', 'tokenize("привет мир")', '["привет", "мир"]', ''),
        ('"hello,world!!!"', 'tokenize("hello,world!!!")', '["hello", "world"]', ''),
        ('"по-настоящему круто"', 'tokenize("по-настоящему круто")', '["по-настоящему", "круто"]', ''),
        ('"2025 год"', 'tokenize("2025 год")', '["2025", "год"]', ''),
        ('"емојі 😊 не слово"', 'tokenize("емојі 😊 не слово")', '["emoji", "не", "слово"]', '(эмодзи выпадают)')
    ]
    
    for input_desc, func_call, expected, comment in test_cases_tokenize:
        print(f"• Вход: {input_desc}")
        print(f"  Вызов: {func_call}")
        print(f"  Ожидаемый результат: {expected}")
        if comment:
            print(f"  Комментарий: {comment}")
        print()
    
    # Тест-кейсы для count_freq + top_n
    print("\n3. ФУНКЦИИ count_freq + top_n:")
    
    
    print("• Тест 1:")
    print("  Вход (токены): [\"a\",\"b\",\"a\",\"c\",\"b\",\"a\"]")
    print("  Промежуточный результат (частоты): {\"a\":3,\"b\":2,\"c\":1}")
    print("  Вызов: top_n(..., n=2)")
    print("  Финальный результат: [(\"a\",3), (\"b\",2)]")
    print()
    
    print("• Тест 2 (тай-брейк):")
    print("  Вход (токены): [\"bb\",\"aa\",\"bb\",\"aa\",\"cc\"]")
    print("  Промежуточный результат (частоты): {\"aa\":2,\"bb\":2,\"cc\":1}")
    print("  Вызов: top_n(..., n=2)")
    print("  Финальный результат: [(\"aa\",2), (\"bb\",2)]")
    print("  Комментарий: (алфавитная сортировка при равенстве)")
    print()

    print("КОНЕЦ ТЕСТ-КЕЙСОВ")



def demo():
    #Демонстрация работы всех функций
    print("ДЕМОНСТРАЦИЯ РАБОТЫ ФУНКЦИЙ")

    
    # Пример 1: Полный цикл обработки
    print("\nПример 1: Полный цикл обработки текста")
    text = "ПрИвЕт\nМИр! Это тестовый текст с числами 2025."
    print(f"Исходный текст: {repr(text)}")
    
    normalized = normalize(text)
    print(f"После normalize: {repr(normalized)}")
    
    tokens = tokenize(normalized)
    print(f"После tokenize: {tokens}")
    
    freq = count_freq(tokens)
    print(f"Частоты: {freq}")
    
    top_words = top_n(freq, 3)
    print(f"Топ-3 слова: {top_words}")
    
    # Пример 2: Обработка с эмодзи
    print("\nПример 2: Обработка с эмодзи")
    text2 = "Python 😊 это круто! Python очень мощный 🚀"
    print(f"Исходный текст: {repr(text2)}")
    
    normalized2 = normalize(text2)
    tokens2 = tokenize(normalized2)
    freq2 = count_freq(tokens2)
    top_words2 = top_n(freq2, 2)
    
    print(f"Токены: {tokens2}")
    print(f"Топ-2 слова: {top_words2}")



if __name__ == "__main__":
    import sys
    
    # Обработка аргументов командной строки
    if len(sys.argv) > 1:
        if sys.argv[1] == "--demo":
            # Режим демонстрации
            print_test_cases()
            demo()
            sys.exit(0)
        elif sys.argv[1] == "--no-cases":
            # Пропускаем вывод тест-кейсов
            skip_cases = True
        else:
            print("Использование:")
            print("  python text.py           - запуск с тест-кейсами и тестами")
            print("  python text.py --demo    - демонстрация работы функций")
            print("  python text.py --no-cases - только тесты без тест-кейсов")
            sys.exit(1)
    else:
        skip_cases = False
        # Выводим тест-кейсы при каждом запуске
        print_test_cases()
    

