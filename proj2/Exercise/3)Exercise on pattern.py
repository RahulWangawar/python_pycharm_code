# Exercise 4
# Pattern Printing
# Input = Integer n
# Boolean = True or False
#
# True n=5
# *
# **
# ***
# ****
#
# False n=5
# ****
# ***
# **
# *

# print("Enter a number")
# a=int(input())
# print("Enter 0 or 1")
# Bool = int(input())
# if Bool==1:
#     Bool==True
# else:
#     Bool==False
# print(Bool)
# if Bool==True:
#     for num in range(a) :
#         print(str("*") * num)
# else:
#     for num in range(a) :
#         print(str("*") * (a - num))

#Using typecasting bool
print("Enter a number")
a=int(input())
print("Enter 0 or 1")
x = int(input())
Bool = bool(x)
print(Bool)

if Bool:
    for num in range(a) :
        print(str("*") * num)
else:
    for num in range(a) :
        print(str("*") * (a - num-1))