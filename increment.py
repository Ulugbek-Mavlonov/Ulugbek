# class Counter:
#     def __init__(self, start, finish):
#         self.start = start
#         self.finish = finish
#
#     def increment(self):
#         self.start += 1
#
#     def get(self):
#         if self.start <= self.finish:
#             return self.start
#         else:
#             return f"Maximal value is reached \nMaximal value {self.finish}"
#
#
# values = Counter(1, 6)
# values.increment()
# values.increment()
# values.increment()
# values.increment()
# values.increment()
# values.increment()
# print(values.get())

# 2
# def multiplay(x,y):
#     return x+y
#
# def count(func, z, k):
#     print(func(z,k))
#
# count(multiplay, 4,5)
# def say(name):
#     return f"Hello {name}"
#
# def be(name):
#     return f"Yo {name}, together we are the awesome"
#
#
# def greet(greeter):
#     return greeter("Bob")
#
#
# print(greet(say))
# print(greet(be))

# def parent():
#     print(f"Printing from the parent() function")
#
#     def first():
#         print(f"Printing from the first() function")
#
#     def second():
#         print(f"Printing from the second() function")
#
#     second()
#     first()
#
# print(parent())

# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"
#
#     def second_child():
#         return "Call me Liam"
#
#     if num == 1:
#         return first_child
#     else:
#         return second_child
#
# # first = parent(1)
# print(parent(1)())
#
# print(parent(8)())

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         print("Something is happening after the function is called.")
#         return func()
#
#     return wrapper
#
#
# @my_decorator
# def say_whee():
#     return "Whee!"
#
#
# # say = my_decorator(say_whee)
# print(say_whee())

def outer_func():
    var = 100

    def inner_func():
        print(f"Printing var from inner_func(): {var}")
        print(f"Printing another_var from inner_func(): {another_var}")

    another_var = 200  # This is defined after calling inner_func()
    inner_func()
    print(f"Printing var from outer_func(): {var}")


outer_func()
