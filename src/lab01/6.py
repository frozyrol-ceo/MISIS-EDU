n_inp = input()
n = int(n_inp.strip())

o, z = 0, 0

for _ in range(n):
    line = input().strip()
    if not line: continue
    parts = line.split()
    if parts[-1] == "True": o += 1
    else: z += 1

print(o, z)


