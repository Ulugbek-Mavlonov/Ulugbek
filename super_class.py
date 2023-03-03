# class Class1():
#     def f_func1(self):
#         print("metod f_func1 class1 ")
#
#
# class Class2(Class1):
#     def f_func2(self):
#         print("metod f_func2 class2 ")
#
#
# class Class3(Class1):
#     def f_func1(self):
#         print("metod f_func1 class3")
#
#     def f_func2(self):
#         print("metod f_func2 class3")
#
#     def f_func3(self):
#         print("metod f_func3 class3")
#
#     def f_func4(self):
#         print("metod f_func4 class3")
#
#
# class Class4(Class2, Class3):
#     def f_func4(self):
#         print("metod f_func4 class4")
#
#
# c1 = Class1()
# c1.f_func1()

# class Subclass:
#     def call_me_s(self):
#         print("Subclass")
#
#
# class LeftSubclass(Subclass):
#     def call_me_l(self):
#         print("LeftSubclass")
#
#
# class RightSubclass(Subclass):
#     def call_me_r(self):
#         print("RightSubclass")
#
#
# class BaseClass(LeftSubclass, RightSubclass):
#     def call_me_b(self):
#         print("BasaClass")
#
#
# searc = LeftSubclass()
# searc.call_me_s()
#
# class Nam:
#     def __init__(self, name, address, age):
#         self.name = name
#         self.address = address
#         self.__age = age
#
#     def get_nam(self):
#         return self.__age
#
#     def set_nam(self, number):
#         self.__age = number
#
#     def add_name(self):
#         self.__age += 3
#
#
# multiplay = Nam("Ulug'bek", "Tashkent", 27)
#
# multiplay.add_name()
# multiplay.add_name()
# multiplay.add_name()
# print(multiplay.get_nam())

class Salon:
    soni=0
    how_m=[]
    def __init__(self, saloni, nomi, narxi):
        self.saloni=saloni
        self.nomi=nomi
        self.narxi=narxi
    def add_avto(self):
        self.soni+=1

    def get_avto(self):
        return f"sizning saloningizda {self.saloni} {self.nomi} nomli {self.soni} ta moshinangiz bor"
    # def how(self,car):


    def result(self):
        return f"sizning {self.how_m} nomli moshinalaringiz bor"



avto1=Salon("GM","malibu",34000)
avto2=Salon("Gm","Jentra",18000)
avto=[avto1,avto2]
for i in avto:



# avto1.add_avto()
# avto1.add_avto()
# avto1.add_avto()
# print(avto1.get_avto())
