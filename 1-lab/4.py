m_str = input("Минуты: ")
m = int(m_str.strip())

hours = m // 60
minutes = m % 60

print(f"{hours}:{minutes:02d}")


