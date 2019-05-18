# outro jeito de resolver isso ao invés de pedir a idade logo no começo
# é setando a idade com um numero > 0 para entrar no while
idade = int(input())
soma = 0
c = 0
media = 0

while idade > 0:
    soma = soma + idade
    c+=1
    idade = int(input())

media = soma / c
print("{:.2f}".format(media))
    
        
        
