#single inheritance- 
#multi level inheritance
#multiple inheritance

#single inheritance- 
class car:
    color = "black"
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
print(car1.color)
