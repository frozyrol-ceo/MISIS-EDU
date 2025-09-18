full = input("ФИО: ")

trimmed = full.strip()
parts = [p for p in trimmed.split() if p]

initials = "".join(part[0].upper() for part in parts) + "."

print(f"Инициалы: {initials}")
len_w_spaces = len("".join(trimmed.split()))
print(f"Длина (символов): {len_w_spaces}")

