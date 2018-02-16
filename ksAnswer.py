import random as rd
import sys

# vars
vars = {}
f = 0
checks = input("Кол-во проверок: ")

ans = input("Вариантов ответов: ")
n = 0
while n != int(ans):                        # sozdanie slovarya
    n += 1
    vars[str(n)] = 0

while f != int(checks):                     # vubor
    n = rd.randint(1,int(ans))
    vars[str(n)] = vars[str(n)] + 1
    f += 1
    sys.stdout.write("Randomizing: {0}%".format(round(f*100/int(checks),2))+'\r')

f = 1
max = 1
print(vars)
while f != len(vars)+1:
    if vars.get(str(f)) > vars.get(str(max)):
        max = f
    f += 1
print('Выбран ответ: ', max)