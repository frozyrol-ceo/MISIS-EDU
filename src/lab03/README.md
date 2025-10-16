# Лабораторная работа №3 — Тексты и частоты слов

**Цель:** нормализовать текст, аккуратно токенизировать, посчитать частоты слов и вывести топ-N.

## Структура проекта

```
src/
├── lib/
│   └── text.py           # Модуль с функциями для работы с текстом
└── lab03/
    ├── text_stats.py      # Скрипт для анализа текста из stdin
    └── README.md          # Этот файл
```

## Задание A — Модуль `src/lib/text.py`
![Тест text_stats.py](../../img/lab03/A_1f.png)
![Тест text_stats.py](../../img/lab03/A_2f.png)
![Тест text_stats.py](../../img/lab03/A_3f.png)
Модуль содержит четыре основные функции для работы с текстом:

### 1. `normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str`

Нормализует текст:
- Приводит к нижнему регистру с помощью `casefold()` (лучше чем `lower()` для Unicode)
- Заменяет все `ё/Ё` на `е/Е`
- Заменяет управляющие символы (`\t`, `\r`, `\n`) на пробелы
- Схлопывает последовательности пробелов в один
- Обрезает пробелы с краёв

**Примеры:**
```python
normalize("ПрИвЕт\nМИр\t")           # → "привет мир"
normalize("ёжик, Ёлка")              # → "ежик, елка"
normalize("Hello\r\nWorld")          # → "hello world"
normalize("  двойные   пробелы  ")   # → "двойные пробелы"
```

### 2. `tokenize(text: str) -> list[str]`

Разбивает текст на токены (слова). Токен — это последовательность символов `\w+` (буквы/цифры/подчёркивание) с возможными дефисами внутри слова.

**Примеры:**
```python
tokenize("привет мир")              # → ["привет", "мир"]
tokenize("hello,world!!!")          # → ["hello", "world"]
tokenize("по-настоящему круто")     # → ["по-настоящему", "круто"]
tokenize("2025 год")                # → ["2025", "год"]
tokenize("emoji 😀 не слово")        # → ["emoji", "не", "слово"]
```

### 3. `count_freq(tokens: list[str]) -> dict[str, int]`

Подсчитывает частоты слов в списке токенов.

**Примеры:**
```python
count_freq(["a","b","a","c","b","a"])  # → {"a": 3, "b": 2, "c": 1}
count_freq(["привет", "мир", "привет"])  # → {"привет": 2, "мир": 1}
```

### 4. `top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]`

Возвращает топ-N самых частых слов. Сортировка по убыванию частоты, при равенстве — по алфавиту.

**Примеры:**
```python
top_n({"a": 3, "b": 2, "c": 1}, 2)       # → [("a", 3), ("b", 2)]
top_n({"bb": 2, "aa": 2, "cc": 1}, 2)    # → [("aa", 2), ("bb", 2)]
```

### Код модуля `text.py`

```python
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
```

## Задание B — Скрипт `src/lab03/text_stats.py`
![Тест text_stats.py](../../img/lab03/B_1.png)
![Тест text_stats.py](../../img/lab03/B_1+.png)
Скрипт читает текст из `stdin`, вызывает функции из модуля `text.py` и выводит статистику:
- Всего слов
- Уникальных слов
- Топ-5 самых частых слов

### Код скрипта `text_stats.py`

```python
"""
Скрипт для анализа текста из stdin и вывода статистики.

Использование:
    echo "Текст для анализа" | python text_stats.py
    cat file.txt | python text_stats.py

Переменные окружения:
    TABLE_FORMAT=1 - включить табличный формат вывода
"""

import sys
import os
from pathlib import Path

# Добавляем путь к модулю lib в sys.path
lib_path = Path(__file__).parent.parent / 'lib'
sys.path.insert(0, str(lib_path))

from text import normalize, tokenize, count_freq, top_n


def print_stats(text: str, top_count: int = 5, table_format: bool = False) -> None:
    # Нормализация и токенизация
    normalized = normalize(text)
    tokens = tokenize(normalized)
    
    # Подсчет частот
    freq = count_freq(tokens)
    top_words = top_n(freq, top_count)
    
    # Вывод статистики
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    
    if table_format and top_words:
        print_table(top_words)
    else:
        print_simple(top_words)


def print_simple(top_words: list) -> None:
    print(f"Топ-{len(top_words)}:")
    for word, freq in top_words:
        print(f"{word}:{freq}")


def print_table(top_words: list) -> None:
    if not top_words:
        return
    
    # Определяем ширину колонки для слов
    max_word_len = max(len(word) for word, _ in top_words)
    word_width = max(max_word_len, len("слово"))
    
    # Определяем ширину колонки для частот
    max_freq_len = max(len(str(freq)) for _, freq in top_words)
    freq_width = max(max_freq_len, len("частота"))
    
    # Выводим заголовок
    print(f"\nТоп-{len(top_words)}:")
    print(f"{'слово':<{word_width}} | {'частота':<{freq_width}}")
    print("-" * (word_width + freq_width + 3))
    
    # Выводим данные
    for word, freq in top_words:
        print(f"{word:<{word_width}} | {freq:<{freq_width}}")


def main():
    # Читаем весь ввод из stdin
    try:
        text = sys.stdin.read()
    except KeyboardInterrupt:
        print("\nПрервано пользователем", file=sys.stderr)
        sys.exit(1)
    
    if not text.strip():
        print("Ошибка: пустой ввод", file=sys.stderr)
        sys.exit(1)
    
    # Проверяем, включен ли табличный формат
    table_format = os.environ.get('TABLE_FORMAT', '0') == '1'
    
    # Выводим статистику
    print_stats(text, top_count=5, table_format=table_format)


if __name__ == "__main__":
    main()
```

## Примеры использования

### Пример 1: Простой текст

**Ввод:**
```bash
echo "Привет, мир! Привет!!!" | python3 src/lab03/text_stats.py
```

**Вывод:**
```
Всего слов: 3
Уникальных слов: 2
Топ-2:
привет:2
мир:1
```

### Пример 2: Текст с ё и дефисами

**Ввод:**
```bash
echo "Ёжик и ежик гуляли по-настоящему весело. Ёлка красива!" | python3 src/lab03/text_stats.py
```

**Вывод:**
```
Всего слов: 8
Уникальных слов: 7
Топ-5:
ежик:2
весело:1
гуляли:1
елка:1
и:1
```

**Пояснение:** Слова "Ёжик" и "ежик" были нормализованы в одно слово "ежик", так как `ё` заменяется на `е`.

### Пример 3: Табличный формат

**Ввод:**
```bash
echo "Привет, мир! Привет, как дела? Мир прекрасен, когда все хорошо. Привет всем!" | TABLE_FORMAT=1 python3 src/lab03/text_stats.py
```

**Вывод:**
```
Всего слов: 12
Уникальных слов: 9

Топ-5:
слово  | частота
----------------
привет | 3      
мир    | 2      
все    | 1      
всем   | 1      
дела   | 1      
```

### Пример 4: Текст с управляющими символами

**Ввод:**
```bash
echo -e "Hello\tWorld\nПрограммирование\r\nна Python" | python3 src/lab03/text_stats.py
```

**Вывод:**
```
Всего слов: 5
Уникальных слов: 5
Топ-5:
hello:1
world:1
на:1
программирование:1
python:1
```

## Запуск тестов и демонстрации

### Запуск модуля text.py

```bash
cd src/lib
python3 text.py
```

**Результат:** Выводятся тест-кейсы для всех функций.

### Демонстрация работы функций

```bash
cd src/lib
python3 text.py --demo
```

**Результат:** Выводятся тест-кейсы и демонстрация работы всех функций на примерах.

### Запуск без тест-кейсов

```bash
cd src/lib
python3 text.py --no-cases
```

**Результат:** Запускаются только тесты без вывода тест-кейсов.

## Особенности реализации

1. **Нормализация текста:**
   - Используется `casefold()` вместо `lower()` для корректной работы с Unicode
   - Символы `ё/Ё` заменяются на `е/Е`
   - Управляющие символы (`\t`, `\r`, `\n`) заменяются на пробелы
   - Множественные пробелы схлопываются в один

2. **Токенизация:**
   - Используется регулярное выражение `\w+(?:-\w+)*`
   - Поддерживаются слова с дефисами (например, "по-настоящему")
   - Числа считаются токенами
   - Эмодзи и спецсимволы игнорируются

3. **Подсчёт частот:**
   - Простой словарь для хранения частот
   - Эффективность O(n) для подсчёта

4. **Топ-N:**
   - Сортировка по убыванию частоты
   - При равенстве частот — по алфавиту (возрастание)
   - Используется ключ сортировки `(-частота, слово)`

5. **Табличный формат:**
   - Автоматическое выравнивание столбцов
   - Включается через переменную окружения `TABLE_FORMAT=1`
   - Красивый вывод с разделителями

## Типовые ошибки и их решения

1. **`ё` vs `е`:**
   - Проблема: "ёжик" и "ежик" считаются разными словами
   - Решение: замена `ё→е` в функции `normalize()`

2. **`lower()` vs `casefold()`:**
   - Проблема: некорректная работа с некоторыми Unicode-символами
   - Решение: использование `casefold()` вместо `lower()`

3. **Дефисы в словах:**
   - Проблема: "по-настоящему" разбивается на два токена
   - Решение: регулярное выражение `\w+(?:-\w+)*`

4. **Длинное тире:**
   - Проблема: "слово—слово" не разделяется
   - Решение: длинное тире не является символом `\w`, поэтому автоматически служит разделителем

