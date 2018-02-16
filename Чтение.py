balance = 0
file = open('save.txt')
files = file.readlines()
balance = int(files[0])
lvl = int(files[1])
exp = int(files[2])
print(balance,lvl,exp,sep='\n')
