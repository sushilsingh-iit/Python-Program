#inheritance- when one class (child/derived) derives the properties & method of another
#class (parent/base).

#class car:
# class toyota(car): # inheritance

class car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")


class toyotacar(car):
    def __init__(self,name):
        self.name = name

car1 = toyotacar("fortuner")
car2 = toyotacar("legender")

print(car1.start())




