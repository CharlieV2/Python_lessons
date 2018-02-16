result = []
for line in open('conf.ini','r'):
    result.extend([str(i) for i in line.split()])
print(result)