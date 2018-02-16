balance = 44000
lvl = 98
exp = 144

save = []
save.append(str(balance))
save.append(str(lvl))
save.append(str(exp))
file = open('save4.txt','w')
file.writelines('%s\n'% i for i in save)
file.close()

file = open('save4.txt','r')
files = file.readlines()
balance = int(files[0])
lvl = int(files[1])
exp = int(files[2])
print('Ваш баланс =',balance)
print('Ваш уровень =',lvl)
print('Ваш опыт =',exp)


