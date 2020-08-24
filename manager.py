from interface import  *


class manager(interface):
    def __init__(self):
        super(manager, self).__init__()
        self.listOfItems = []
    def viewItem(self):
        for i in self.itemFile:
            self.listOfItems = eval(i)
            temp='{name:20}{price:15}{quantity:20}'
            print('Name of Product    ','Price      ','Quantity       ')
            print('===============================================')
        for j in range(len(self.listOfItems)):
               # print('name of item               ','price             ','quantity')
                #print(self.listOfItems[j][0],'                  ',self.listOfItems[j][1],'               ',self.listOfItems[j][2])
                print(temp.format(name=self.listOfItems[j][0],price=self.listOfItems[j][1],quantity=self.listOfItems[j][2]))
    def addItem(self):
        l = []
        print('Enter the name of product: ',end='')
        name = super().inputString()
        print('Enter price: ',end = '')
        price = super().inputInteger()
        print('enter quantity: ',end = '')
        quantity = super().inputInteger()
        l.extend((name,price,quantity))
        self.listOfItems.append(l)
        return self.listOfItems
class write(manager):
    def writer(self):
        f= open('myfile.txt','a+')
        print('iam run')
        w = super().addItem()
        f.write(str(w))


m=manager()
m.viewItem()
#m.viewItem()
#m.addItem()
#m.viewItem()
n=write()
n.writer()

m.viewItem()