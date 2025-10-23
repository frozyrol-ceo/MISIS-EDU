from collections import Counter
import os
import sys
from pathlib import Path
import csv
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
        
    Raises:
        FileNotFoundError: Если файл не найден
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


def write_report_to_csv(word_counts: List[Tuple[str, int]], path: str | Path = "report.csv") -> None:
    """
    Записывает отчет о частоте слов в CSV файл.
    
    Args:
        word_counts: Список кортежей (слово, количество) отсортированный по частоте
        path: Путь к файлу для записи отчета (по умолчанию "report.csv")
        
    Raises:
        IOError: Если не удается записать файл
    """
    try:
        p = Path(path)
        with p.open("w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(("word", "count"))
            for word, count in word_counts:
                writer.writerow((word, count))
    except IOError as e:
        print(f"Ошибка при записи файла: {e}")
        raise


def analyze_and_report(input_file: str, output_file: str = "report.csv") -> None:
    """
    Анализирует текстовый файл и создает CSV отчет.
    
    Args:
        input_file: Путь к анализируемому файлу
        output_file: Путь к файлу отчета (по умолчанию "report.csv")
    """
    try:
        # Читаем текст из файла
        text = read_text(input_file)
        
        # Подсчитываем частоты слов
        frequencies = frequencies_from_text(text)
        
        # Сортируем по частоте
        sorted_counts = sorted_word_counts(frequencies)
        
        # Записываем отчет в CSV
        write_report_to_csv(sorted_counts, output_file)
        
        print(f"Отчет сохранен в файл: {output_file}")
        print(f"Обработано слов: {len(sorted_counts)}")
        
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при обработке: {e}")
        sys.exit(1)


def main():
    """Основная функция программы."""
    # Путь к файлу по умолчанию
    default_input = "data/samples/input.txt"
    default_output = "src/lab04/report.csv"
    
    # Проверяем аргументы командной строки
    if len(sys.argv) == 1:
        # Используем файлы по умолчанию
        input_file = default_input
        output_file = default_output
    elif len(sys.argv) == 2:
        # Передан только входной файл
        input_file = sys.argv[1]
        output_file = default_output
    elif len(sys.argv) == 3:
        # Переданы оба файла
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    else:
        print("Использование:")
        print("  python io_report.py                           - анализ файла по умолчанию")
        print("  python io_report.py <input_file>              - анализ указанного файла")
        print("  python io_report.py <input_file> <output_file> - анализ с указанием выходного файла")
        sys.exit(1)
    
    print(f"Анализ файла: {input_file}")
    print(f"Выходной файл: {output_file}")
    
    analyze_and_report(input_file, output_file)


if __name__ == "__main__":
    main()