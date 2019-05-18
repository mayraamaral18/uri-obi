maior = 0
c = 0

for v in range (100):
    
    valor = int(input())

    if valor > maior:
        maior = valor
        c = v+1

print(maior)
print(c)
