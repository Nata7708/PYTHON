# Дано натуральное число. Напишите программу, которая вычисляет:
# количество цифр 3 в нем;
# сколько раз в нем встречается последняя цифра;
# количество четных цифр;
# сумму его цифр, больших пяти;
# произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
# сколько раз в нем встречается цифры 0 и 5 (всего суммарно).
# Формат входных данных
# На вход программе подается одно натуральное число.

n = int(input())
count_sum_bolshe_5 = 0
count_3 = 0
count_last = 0
last = n % 10
count_proizv_7 = 1
count_col_5 = 0
count_chet = 0
while n != 0:
    a = n % 10
    if a == 3:
        count_3 += 1
    if a == last:
        count_last += 1
    if a % 2 == 0:
        count_chet += 1
    if a > 5:
        count_sum_bolshe_5 += a
    if a > 7:
        count_proizv_7 *= a
    if a in (0, 5):
        count_col_5 += 1
    n = n//10
print(count_3)
print(count_last)
print(count_chet)
print(count_sum_bolshe_5)
print(count_proizv_7)
print(count_col_5)