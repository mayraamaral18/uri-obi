n = []

for i in range (100):

    n.append(float(input()))

for i2 in range (len(n)):

    if (n[i2] <= 10):

        print("A[{}] = {}".format(i2,n[i2]))
