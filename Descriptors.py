# from turtle import Turtle, Screen
#
# tippy = Turtle()
#
# tippy.shape("turtle")
# tippy.color("red")
# tippy.forward(100)
# tippy.back(20)
#
# MS = Screen()
# MS.exitonclick()

# def make_payment(a, b):
#     for i in range(a):
#         yield a + b
#         a = a + 1
#
#
# m = make_payment(5, 8)
#
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))

# def squares(n):
#     for i in range(n):
#         yield i**2
#
#
# g = squares(10)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# import random
#
#
# def random_int(low, high, n):
#     for ele in range(n):
#         yield random.randint(low, high)
#
#
# for i in random_int(20, 100, 5):
#     print(i)

# s = "tejas"
#
# p = list(iter(s))
# print(p)

# def deco(orig):
#     def wrap_func():
#         orig()

# def add(n1, n2):
#     return n1 + n2


# def mul(n1, n2):
#     return n1 * n2

#
# def calc(n1, n2, func):
#     return func(n1, n2)
#
# print(calc(5, 6, add))

# def deco(func):
#     def wraper(*args):
#         func(*args)
#         print(func(*args))
#     return  wraper
#
# @deco
# def mul(n1, n2):
#     print("hello")
#     return n1 * n2
#
# mul(2,4)

# class NonNegativeValue(object):
#     def __init__(self, val):
#         self.val = val
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         return self.val
#
#     def __set__(self, instance, value):
#         if not isinstance(value, int):
#             raise TypeError("typooo")
#
#         if value < 0 :
#             raise ValueError("less than zerooo")
#
#         self.val = value
class Lables(object):
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.value

    def __set__(self, instance, value):
        if value == "'INBOX'":
            self.value = value
        if value == "'sent items'":
            self.value = value


class Tags(object):
    value = Lables()

    def valuess(self, vl):
        self.value = vl
        print(self.value)


v = Tags()
v.valuess("'sent items'")

# class Name_Caps(object):
#     # def __init__(self,*val):
#     #     self.val = val
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         return self.value
#
#     def __set__(self, instance, value):
#         if len(value) <= 8 :
#             raise ValueError("lenght must be more than 8 chr long")
#         self.value = value
#
# class Angle(object):
#     name = Name_Caps()
#     # def __init__(self,name):
#     #     self.name = name
#
#     def p_name(self,vl):
#         self.name = vl
#         print(vl)


# s = Angle()
# print(s.name)
# # s.name = "123459789"
# # print(s.p_name)
# s.p_name("tejas")
# class Tejas(object):
#     age = NonNegativeValue(24)
#
# t = Tejas()
# print(t.age)
# t.age = 23
# print(t.age)
