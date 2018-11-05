InputNumber = int(input('Число в десятичной СС: '))
NumSys = int(input('Перевести в СС: '))

List = ["A", "B", "C", "D", "E", "F", "G", ]
ResultNumber = ''

while InputNumber >= NumSys:
    Temp = InputNumber % NumSys
    if (Temp >= 10):
        Temp = List[(Temp%10)]
        
    ResultNumber = str(Temp) + ResultNumber
    InputNumber = InputNumber // NumSys

ResultNumber = str(InputNumber) + ResultNumber

print(ResultNumber)