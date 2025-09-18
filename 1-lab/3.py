def parse_number(text: str) -> float:
    return float(text.strip().replace(",", "."))


p = parse_number(input("price: "))
d = parse_number(input("discount: "))
v = parse_number(input("vat: "))

base = p * (1 - d / 100)
vat_amount = base * (v / 100)
total = base + vat_amount

print(f"База после скидки: {base:.2f} ₽")
print(f"НДС:               {vat_amount:.2f} ₽")
print(f"Итого к оплате:    {total:.2f} ₽")


