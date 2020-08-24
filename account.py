class writeToFile:
    def SaveToFile(self,filename,obj):
        f=open(filename,'a')
        for item in obj:
            f.write(str(item)+'\n')
        f.close()

class readFromFile:
    def read(self,fileName):
        self.obj=[]
        f=open(fileName ,'r')
        for line in f:
                self.obj.append(eval(line))
        f.close()
        return self.obj
class account:
    d=readFromFile()
    def __init__(self):
         self.details= self.d.read('loginDetails' )
    def verify(self,userName,Password):
        for eachItem in self.details:
            if userName==eachItem[2]:
                if Password==eachItem[3]:
                    return True

class Login(account):
    def login(self):
            self.name=input('enter username:')
            self.password=input('enter password')
            if self.verify(self.name,self.password)==True:
                return
            else:
                print('You need to sign up first')
class SignUp(account):
    def signup(self):
        detail=[]
        f=writeToFile()

        Fname=input('enter first name:')
        Lname=input('enter Last name:')
        Address=input('enter email address:')
        password=input('enter password:')
        detail.append(Fname)
        detail.append(Lname)
        detail.append(Address)
        detail.append(password)
        f.SaveToFile('loginDetails',detail)


s=SignUp()
s.signup()



