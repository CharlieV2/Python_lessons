InputNumber = int(input('Число в десятичной СС: '))
NumSys = int(input('Перевести в СС: '))

List = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ]
ResultNumber = ''

while InputNumber >= NumSys:
    Temp = InputNumber % NumSys
    if (Temp >= 10):
        if (Temp >= 20):
            Temp = List[(Temp%10) + 10]
        else:
            Temp = List[(Temp%10)]
        
        
    ResultNumber = str(Temp) + ResultNumber
    InputNumber = InputNumber // NumSys

ResultNumber = str(InputNumber) + ResultNumber

print(ResultNumber)
