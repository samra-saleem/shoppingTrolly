

class interface:
    def __init__(self):
        self.itemFile = open('myfile.txt','r')
        self.managerFile = open('managerDetails.txt','r')

    def MainMenu(self):
        print('*** Welcome to our Online store ***')
        print('Print 1 for manager and 2 for customer.')
    def managerMenu(self):
        print('hello manager!')
    def inputInteger(self):
        loop = True
        while loop:
            try:
                self.value1 = int(input())
                loop = False
            except:
                print('enter Intger value only!!')
            else:
                return self.value1

    def inputString(self):
        regex = '@_!#$%^&*()<>?/\|}{~:'
        loop = True
        while loop:
            self.value2 = input()
            if self.value2.isdigit() or self.value2 in regex :
                 print('Invalid Entry !!')
                 continue
            elif self.value2 == '':
                print('write something !!')
            else:
                loop = False

                return self.value2


class check(interface):
    def checker(self):
        s = super().inputInteger()
        print(s)


a=interface()
c= check()

