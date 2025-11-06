import json
import csv


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    if json_path[-4::] != 'json' or csv_path[-3::] != 'csv':
        raise TypeError
    with open(json_path, encoding="utf-8") as f: 
        data = json.load(f)
    if not data or type(data[0]) != dict:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    with open(csv_path, "w", newline="", encoding="utf-8") as cf:
        writer = csv.DictWriter(cf, fieldnames=list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)


json_to_csv('data/samples/test.json', 'src/lab05/json_to_csv_converted_file.csv')


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    if csv_path[-3::] != 'csv' or json_path[-4::] != 'json':
        raise TypeError
    lt_rows = []
    with open(csv_path, 'r', encoding='utf-8') as cf:
        reader = csv.DictReader(cf)
        for row in reader:
            lt_rows.append(row)
        if not lt_rows:
            raise ValueError
    with open(json_path, 'w', encoding='utf-8') as jf:
        json.dump(lt_rows, jf, ensure_ascii=False, indent=2)


csv_to_json('data/samples/test.csv', 'src/lab05/csv_to_json_example.json')