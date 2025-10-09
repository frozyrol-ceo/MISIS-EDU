vinp = input('in: ')
w = ''
i1 = 0 
i2 = 0

for i in range(len(vinp)):
    if vinp[i].isupper():
        i1 = i 
        break
    else:
        continue 
for i in range(len(vinp)):
    if vinp[i] in '0123456789':
        i2 = i+1
        break
    else:
        continue
shag = i2 - i1
for i in range(i1,len(vinp),shag):
    w+=vinp[i]
print(f'out: {w}')