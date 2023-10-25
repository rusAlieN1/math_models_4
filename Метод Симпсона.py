import numpy as np

print("Введите координату 1 точки отсчёта:")
a = float(input())
print("Введите координату 2 точки отсчёта:")
b = float(input())
print("Введите желаемую погрешность:")
fault = float(input())


def find_definition(a, b, N):
    h = (b - a) / (2 * N)
    partial_S1 = 0
    for i in np.arange(a + h, b, 2 * h):
        partial_S1 = partial_S1 + F(i)
    partial_S2 = 0
    for j in np.arange(a + 2 * h, b, 2 * h):
        partial_S2 = partial_S2 + F(j)
    part_definition = h / 3 * (F(a) + F(b) + 4 * partial_S1 + 2 * partial_S2)
    return part_definition


def F(x): return 5 * x ** 2 + x + 1


N = 1
sum1 = find_definition(a, b, N)
while True:
    N *= 2
    sum2 = find_definition(a, b, N)
    if abs(sum2 - sum1) < fault:
        break
    sum1 = sum2

print("Значение определённого интеграла:", sum2)
print("Количество итераций:", N)
