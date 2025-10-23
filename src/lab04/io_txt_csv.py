from collections import Counter
import os
import sys
from pathlib import Path
from typing import List, Tuple

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.text import tokenize, normalize


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Читает текст из файла.
    
    Args:
        path: Путь к файлу
        encoding: Кодировка файла (по умолчанию utf-8)
        
    Returns:
        Содержимое файла как строка
    """
    p = Path(path)
    return p.read_text(encoding=encoding)


def frequencies_from_text(text: str) -> dict[str, int]:
    """
    Подсчитывает частоты слов в тексте.
    
    Args:
        text: Исходный текст
        
    Returns:
        Словарь с частотами слов
    """
    tokens = tokenize(normalize(text))
    return Counter(tokens)


def sorted_word_counts(freq: dict[str, int]) -> List[Tuple[str, int]]:
    """
    Сортирует слова по частоте (убывание), затем по алфавиту.
    
    Args:
        freq: Словарь с частотами слов
        
    Returns:
        Отсортированный список кортежей (слово, частота)
    """
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def format_word_table(word_counts: List[Tuple[str, int]]) -> None:
    """
    Выводит таблицу слов и их частот в красивом формате.
    
    Args:
        word_counts: Список кортежей (слово, частота)
    """
    if not word_counts:
        print("Нет данных для отображения")
        return
    
    # Находим максимальную длину слова
    max_word_length = max(len(word) for word, _ in word_counts)
    
    # Вычисляем ширину колонки для слов (с небольшим запасом)
    word_column_width = max(max_word_length + 2, 8)
    
    # Заголовок таблицы
    print(f"{'word':<{word_column_width}}count")
    print("-" * (word_column_width + 5))
    
    # Строки таблицы
    for word, count in word_counts:
        print(f"{word:<{word_column_width}}{count}")


def analyze_text_file(file_path: str) -> None:
    """
    Анализирует текстовый файл и выводит статистику по словам.
    
    Args:
        file_path: Путь к анализируемому файлу
    """
    try:
        # Читаем текст из файла
        text = read_text(file_path)
        
        # Подсчитываем частоты слов
        frequencies = frequencies_from_text(text)
        
        # Сортируем по частоте
        sorted_counts = sorted_word_counts(frequencies)
        
        # Выводим таблицу
        format_word_table(sorted_counts)
        
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден")
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")


def main():
    """Основная функция программы."""
    # Путь к файлу по умолчанию
    default_file = "data/samples/input.txt"
    
    # Проверяем, передан ли путь к файлу как аргумент командной строки
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = default_file
    
    print(f"Анализ файла: {file_path}")
    print("=" * 50)
    
    analyze_text_file(file_path)


if __name__ == "__main__":
    main()