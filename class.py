class Shop:
    count = 0
    def __init__(self, name, count):
        self.name = name
        self.count = count
    def sell(self):
        print('%s sell product'%self.name)
        self.count += 1
        Shop.count += 1
    def info(self):
        print('All selled:',Shop.count)
        print(self.name,'selled:',self.count)
argo = Shop('ARGO')
sever = Shop('SEVER')
