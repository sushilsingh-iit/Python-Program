class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real,"i+",self.img,"j")


num1 = complex(1,2)
num1.shownumber()

num1 = complex(4,6)
num1.shownumber()