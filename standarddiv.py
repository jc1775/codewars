from math import sqrt


def std(x):
    n = len(x)
    m = sum(x) / n
    topsum = 0
    for i in range(n):
        topsum += (x[i] - m)**2
    return sqrt(topsum / (n))


test = [32,64,234,123,5764,2342,1231,623,124,634,845]
print(std(test))