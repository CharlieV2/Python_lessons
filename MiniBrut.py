import random as rd
import sys
abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
results = []


fc = 'A'
sc = 'A'
tc = 'A'
s = 0

for tc in abc:
    results.append(fc+sc+tc)

    
    for sc in abc:
        results.append(fc+sc+tc)

        
        for fc in abc:
            results.append(fc+sc+tc)


#print(results)
print(len(results))

twins = 0
errors = 0
cmp = 0

while True:
    a = str(abc[rd.randint(0,len(abc)-1)]+
            abc[rd.randint(0,len(abc)-1)]+
            abc[rd.randint(0,len(abc)-1)])
    cmp += 1
    sys.stdout.write("Проверяется: "+a+" Проверено: "+str(cmp)+' Ошибок: '+str(errors)+" Дупликаты: "+str(twins)+'\r')
    check = 0
    
    for g in results:
        if g == a:
            check += 1

    if check == 0 :
        errors += 1
    
    if check > 1:
        twins += 1