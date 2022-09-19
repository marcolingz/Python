# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# L1 = [1,2,3,4]
# L2 = [1,2,5,6]
# for e in L1:
#     if e in L2:
#         L1.remove(e)

# def fact(n):
#     assert not n==0, "input can't be zero!"
#     if n == 1:
#         return 1
#     else:
#         return n*fact(n-1)
    
# print(fact(5))

# def printMove(fr, to):
#     print ("Move from "+str(fr)+" to "+str(to))

# def Towers(n, fr, to, spare):
#     if n == 1:
#         printMove(fr, to)
#     else:
#         Towers(n-1, fr, spare, to)
#         Towers(1, fr, to, spare)
#         Towers(n-1, spare, to, fr)

# Towers(4, "Fr", "To", "S")

# def fib(x):
#     if x==1 or x==0:
#         return 1
#     else:
#         return fib(x-1)+fib(x-2)

# print(fib(12))

# def isPalindrome(s):
#     def toChars(s):
#         s = s.lower()
#         ans = ''
#         for c in s:
#             if c in 'abcdefghijklmnopgrstuvwxyz':
#                 ans = ans + c
#         return ans

#     def isPal(s):
#         if len(s) <= 1:
#             return True
#         else:
#             return s[0] == s[-1] and isPal(s[1:-1])
#         return isPal(toChars(s))
    
#     return isPal(s)
    
# print(isPalindrome("a b c bd a"))

# class coordinate(object):
#     def __init__(self, x, y):
        
#         self.x = x
#         self.y = y
    
#     def __str__(self):
#         return "("+str(self.x)+","+str(self.y)+")"
        
#     def distance(self, other):
#         x_diff_sq = (self.x - other.x)**2
#         y_diff_sq = (self.y - other.y)**2
#         return(x_diff_sq + y_diff_sq)**0.5
#     def __eq__(self, other):
#         if (self.x == other.x) & (self.y == other.y):
#             return True
#         else:
#             return False

# c = coordinate(1,1)
# d = coordinate(2,2)
# print("The distance between "+str(c)+" and "+str(d)+" is:")
# print(c.distance(d))
# print("C == D is "+str(c==d))

# class Fraction(object):
#     def __init__(self, num, denom):
#         assert type(num) == int and type(denom) == int
#         self.num = num
#         self.denom = denom

#     def __str__(self):
#          return "("+str(self.num)+","+str(self.denom)+")"
 
#     def __add__(self, other):
#         top = self.num * other.denom + self.denom * other.num
#         butt = self.denom * other.denom
#         return Fraction(top, butt)

# a = Fraction(2,3)
# b = Fraction(1,4)
# print(a+b)

class Animal (object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name (self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name (self, newname=""):
        self.name = newname
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)

class Cat(Animal):
    tag = 1
    def __init__(self, age):
        Animal.__init__(self, age)
        Cat.tag += 1
    def Speak(self):
        print("Meow")
    def __str__(self):
        return "Cat:"+str(self.name)+":"+str(self.age)
    
a = Animal(3)
a.set_name("cat")
print(a)
c = Cat(2)
c.set_name("fluffy")
print(c.tag)
d = Cat(3)
print(d.tag)
print(c.get_name())    