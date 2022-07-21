# Дано натуральное число nn. Напишите программу, которая печатает численный треугольник
n = int(input())
for i in range(1, n+1):
    for j in range(1, i+ 1):
        print(i, end='')
    print()