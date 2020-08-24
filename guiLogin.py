from tkinter import *
from main import *
class Login(account):
    def loginAccount(self):
            self.name=input('enter username:')
            self.password=input('enter password')
            if self.verify(self.name,self.password)==True:
                return
            else:
                print('You need to sign up first')


class Account(Tk):
    l=Login()
    def __init__(self):
        super().__init__()
        self.title('login system')
        self.minsize(400,400)
        self.maxsize(800,800)
        self.login()
        self.mainloop()
    def login(self):
        button=Button(self,text='login',width=5,height=2,fg='white' , bg='black',command=self.l.loginAccount)
        button.pack()
a=Account()