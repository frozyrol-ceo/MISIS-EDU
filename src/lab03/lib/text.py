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


if __name__ == "__main__":
    # Запуск тестов
    import doctest
    doctest.testmod()



    # normalize
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"
    assert normalize("Hello\r\nWorld") == "hello world"
    assert normalize("  двойные   пробелы  ") == "двойные пробелы"
    

    # tokenize
    assert tokenize("привет, мир!") == ["привет", "мир"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]
    

    # count_freq + top_n
    freq = count_freq(["a", "b", "a", "c", "b", "a"])
    assert freq == {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]
    

    # тай-брейк по слову при равной частоте
    freq2 = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert top_n(freq2, 2) == [("aa", 2), ("bb", 2)]
    


    print("\nВсе тесты успешно пройдены! ✓")

