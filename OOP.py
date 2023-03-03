# class Person:
#     def __init__(self, name, age, jinsi, malumoti, ishjoyi):
#         self.name = name
#         self.age = age
#         self.jinsi = jinsi
#         self.malumoti = malumoti
#         self.ishi = ishjoyi
#
#
# key = Person('Ali', 34, 'erkak', 'oliy', 'ishsiz')
# all = Person('Lola', 45, 'ayol', "o'rta", 'nafaqada')
#
# print(f"{key.name} {key.age} yoshda,jinsi {key.jinsi}, malumoti {all.malumoti} va hozir {key.ishi}")
# print(f"{all.name} {all.age} yoshda,jinsi {all.jinsi}, malumoti {key.malumoti} va hozir {all.ishi}")

class Car:
    def __init__(self, color, miles):
        self.color = color
        self.miles = miles
    def __str__(self):
        return f"this {self.color} car {self.miles} miles "
#
#
car1 = Car('red', 10000)
car2 = Car('blue', 200000)
# for i in (car1,car2):
#     print(f"this {i.color} car {i.miles} miles ")

print(car1,car2)

# class Book:
#     books = []
#
#     def __init__(self, k):
#         pass
#
#     def add_book(self, k):
#         self.books.append(k)
#
#     def get_books(self):
#         pass
#
#
# coin = Book('DeylKarnegi')
#
# print
# import math
#
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def calculate_distance(self, z):
#         # p1.calculate_distance(p2)
#         return math.sqrt((self.x - p2.x) ** 2 + (self.y - p2.y)**2)
#
#         # print(z)
#
#
# p1 = Point(0, 0)
# p2 = Point(6, 8)
# k = p1.calculate_distance(p1)
# print(k)
# z=sqrt((x2-int(x1))**2+(y2-int(y1))**2)
