# Дано натуральное число. Напишите программу, которая вычисляет:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.
n = int(input())
countSum = 0
countColvo = 0
countProizv = 1
lastN = n % 10
while n != 0:
    firstN = n % 10
    countSum += firstN
    countColvo +=1
    countProizv = countProizv * firstN
    n = n//10
sredArifm = countSum / countColvo
sumFirstLast = lastN+firstN
print(countSum, countColvo, countProizv, sredArifm, firstN, sumFirstLast, sep = '\n')
