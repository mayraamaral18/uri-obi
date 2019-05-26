def rafael(x, y):

    return (3*x)**2 + y**2

def beto(x, y):

    return 2*(x**2) + (5*y)**2

def carlos(x, y):

    return -100*x + y**3

n = int(input())

for i in range (n):

    x, y = [int(x) for x in input().split(' ')]

    maior = max(rafael(x, y), beto(x, y), carlos(x, y))

    if(maior == rafael(x, y)):

        print("Rafael ganhou")

    if(maior == beto(x, y)):

        print("Beto ganhou")

    if (maior == carlos(x, y)):

        print("Carlos ganhou")
    
