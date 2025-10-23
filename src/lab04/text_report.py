from collections import Counter
import os, sys
from pathlib import Path
import csv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.text import tokenize, normalize



def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    функция для чтения текста из файла
    используем исключения для обработки несуществующего файла
    """
    try:
        p = Path(path)
        return p.read_text(encoding=encoding)
    except FileNotFoundError:
        print('Такого файла не существует.')
        sys.exit(-1)

new_str = read_text("data/samples/input.txt")


def frequencies_from_text(text: str) -> dict[str, int]:
    tokens = tokenize(normalize(text))
    return Counter(tokens) 

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

def write_report_to_csv(word_counts: list[tuple[str, int]], path: str | Path = "report.csv") -> None:
    """
    Функция для записи отчета о частоте слов в CSV файл
    word_counts: список кортежей (слово, количество) отсортированный по частоте
    path: путь к файлу для записи отчета (по умолчанию "report.csv")
    """
    p = Path(path)
    with p.open("w", newline='', encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(("word", "count"))
        for word, count in word_counts:
            w.writerow((word, count))

sorted_list = sorted_word_counts(frequencies_from_text(new_str))

write_report_to_csv(sorted_list, "src/lab04/report.csv")
print(f"Отчет сохранен в файл: report.csv")