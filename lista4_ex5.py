qt_2 = 0
qt_3 = 0
qt_4 = 0
qt_5 = 0

e = int(input())

n = [int(x) for x in input().split(' ')]

for i in (n):

    if(i % 2 == 0):

        qt_2 +=1

    if(i % 3 == 0):

        qt_3 +=1

    if(i % 4 == 0):

        qt_4 +=1

    if(i % 5 == 0):

        qt_5 +=1

print(qt_2, "Multiplo(s) de 2")
print(qt_3, "Multiplo(s) de 3")
print(qt_4, "Multiplo(s) de 4")
print(qt_5, "Multiplo(s) de 5")
