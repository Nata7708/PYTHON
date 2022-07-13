# Назовем число красивым, если оно является четырехзначным и делится нацело на 77 или на 1717. 
# Напишите программу, определяющую, является ли введённое число красивым. 
# Программа должна вывести «YES», если число является красивым, или «NO» в противном случае.
x = int(input())
if (10000>x>999) and (x % 7 == 0 or x % 17 == 0):
    print('YES')
else:
    print('NO')