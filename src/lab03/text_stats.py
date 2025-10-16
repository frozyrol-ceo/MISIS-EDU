import sys
import os
from pathlib import Path

# Добавляем путь к модулю lib в sys.path
lib_path = Path(__file__).resolve().parent.parent / 'lib'
sys.path.insert(0, str(lib_path))

from text import normalize, tokenize, count_freq, top_n  # type: ignore


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
        print()  # Пустая строка перед таблицей
        print_table(top_words)
    else:
        print_simple(top_words)


def print_simple(top_words: list) -> None:
    print("Топ-5:")
    for word, freq in top_words:
        print(f"{word}:{freq}")


def print_table(top_words: list) -> None:
    if not top_words:
        return
    
    # Определяем ширину колонки для слов (по максимальной длине слова из топа)
    max_word_len = max(len(word) for word, _ in top_words)
    word_width = max(max_word_len, len("слово"))
    
    # Определяем ширину колонки для частот
    max_freq_len = max(len(str(freq)) for _, freq in top_words)
    freq_width = max(max_freq_len, len("частота"))
    
    # Выводим заголовок
    print("Топ-5:")
    print(f"{'слово':<{word_width}} | {'частота':<{freq_width}}")
    print("-" * (word_width + freq_width + 3))
    
    # Выводим данные
    for word, freq in top_words:
        print(f"{word:<{word_width}} | {freq:<{freq_width}}")


def main():
    """Основная функция программы."""
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


