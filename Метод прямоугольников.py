import numpy as np

print("Введите координату 1 точки отсчёта:")
a = float(input())
print("Введите координату 2 точки отсчёта:")
b = float(input())
print("Введите желаемую погрешность:")
fault = float(input())


def find_definition(a, b, n):
    partial_sum1 = 0
    for i in np.arange(a, b, (b - a) / n):
        Ss = (b - a) / n * F(i + (b - a) / (2 * n))
        partial_sum1 = partial_sum1 + Ss
    return partial_sum1


def F(x): return 5 * x ** 2 + x + 1


N = 1
sum1 = find_definition(a, b, N)
while True:
    N *= 2
    sum2 = find_definition(a, b, N)
    if abs(sum2 - sum1) < fault:
        break
    sum1 = find_definition(a, b, N)

print("Значение определённого интеграла:", sum2)
print("Количество итераций:", N)
