# LECATURE 1

# CODE 1

# num1 = int(input("Enter the no.:"))
# num2 = int(input("Enter the no.:"))

# sum = num1 + num2

# print ("you sum is:", sum)

#Code 2

# sq = int(input("Enter the square:"))

# area = sq*sq

# print ("The area of squre is:", area)

# Code 3

# no1 = float(input("Enter the no:"))
# no2 = float(input("Enter the no:"))

# avg = (no1 + no2) / 2

# print ("The average is", avg)

#Cod 4

# a = int(input("Enter the no:"))
# b = int(input("Enter the no:"))

# print ("Ans is:", a>=b) or ("ANs is", a>b)

# LECATURE 2

#Code 5

# name = "Hi, My name is $ symbol $ only $99.99"
# print (name.count("$"))

# print (len(name))

# Code 6

# num = int(input("Enter the no:"))

# if (num%2==0):
#     no = "Even"
# else:
#     no = "Odd"

# print (no)

#Code 7

# no1 = int(input("Enter the 1st no:"))
# no2 = int(input("Enter the 2nd no:"))
# no3 = int(input("Enter the 3rd no:"))
# no4 = int(input("Enter the 3rd no:"))

# if (no1 > no2 and no1 > no3 and no1 > no4):
#     print (no1, "no1 greater")

# elif (no2 > no3 and no2 > no4):
#     print (no2,"no2 is greater")

# elif (no3 > no4):
#     print (no3,"no3 is greater")
# else:
#     print (no4, "no4 is greater")


# Code 8

# no = int(input("Enter your no:"))

# if no % 7 == 0:
#     print ("No",no,"is divisible and multiple of 7")
# else:
#     print ("No",no,"is not divisible and not multiple of 7")

# LECATURE 3

# Code 9

# mov1 = str(input("Enter you fav movie_1:"))
# mov2 = str(input("Enter you fav movie_2:"))
# mov3 = str(input("Enter you fav movie_3:"))

# list = [mov1, mov2, mov3]
# print (list)

#Code 10

# ls_1 = [2,4,6,4,2]
# ls_2 = [2,4,6,8,4]

# copy_lis_1 = ls_1.copy()
# copy_lis_1.reverse()

# if (copy_lis_1 == ls_1):
#     print ("Palindraome")
# else:
#     print ("Not a palindrom")

# Code 11

# tuple = ("C","D","A","A","B","B","A")
# print (tuple.count("A"))
# print (type(tuple))


# list = ["C","D","A","A","B","B","A"]
# list.sort()
# print (list)
# print (type(list))

# LECTURE 4

# Code 12


# dict = {"table" : ["a piece of furniture, list of facts nd figure"], 
#     "cat" : "a small animal"
#     }

# print (dict)
# print (type(dict))

# Code 13
 
# set = {
#     "python", "java", "C++", "python", "JS", "java", "python", "java", "C++", "C"
# }

# print (set)
# print (type(set))
# print (len(set))

# Code 14   

# AI = float(input("Enter the marks of AI:"))
# MAT = float(input("Enter the marks of MAT:"))
# SCI = float(input("Enter the marks of SCI:"))

# dict = {}

# dict.update({"AI" : AI}) 
# dict.update({"MAT" : MAT})
# dict.update({"SCI" : SCI})

# print (type(dict))
# print (len(dict))
# print (dict)

# Code 15

# set = {9, "9.0"}    # Method 1

# print (type(set))
# print (set)
# print (len(set))


# set = {             # Method 2
#     ("int", "9"),
#     ("float", "0.9")
# }    

# print (type(set))
# print (set)
# print (len(set))


# LECTURE 5

# Code 16
# n = 1
# while (n<=100):
#     print (n)
#     n += 1
# print ("END")

# Code 17
# n = 100

# while (n>=1):
#     print (n)
#     n -= 1
# print ("END")

# n = int(input("Enter the no:"))
# i = 1
# print ("The table of",n, "is:")
# while i<=10:
#     print (n ,"*", i, "=", n*i)
#     i+=1

#Code 18

# list = [1, 4, 9, 16, 35, 36, 49, 64, 81, 100]
# idx = 0     # This is knows as traverse
# while idx < len(list):
#     print (list[idx])
#     idx +=1

# Code 19

# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for i in list:
#     print (i)
# else:
#     print ("END")


# Code 20

# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100,)
# x = int(input("Enter the no: "))
# idx = 0

# for val in tup:
#     if (val == x):
#         print ("Found",x,"@ index", idx)
#         break
#     else:
#         print ("Not found @ index:", idx)
#     idx += 1

# print ("CODE ENDED")

# Code 21

# n = int(input("Enter the no: "))
# for i in range (1,11):
#     print (n*i)


# Code 22
# Program to find the sum of natural numbers

# Input: Number of terms (N)
# N = int(input("Enter a natural number: "))

# # Initialize variables
# sum_n = 0
# i = 1

# # While loop to calculate sum
# while i <= N:
#     sum_n += i
#     i += 1

# # Output the result
# print(f"The sum of natural numbers up to {N} is: {sum_n}")


# CODE 23
# n = int(input("Enter the no: "))
# fact = 1

# for i in range (1,n+1):
#     fact *= i

# print ("The factorial is =",fact)

# CODE 24
# S = 1
# for S in range (1,7):
#     print("Table of:",S)
#     for R in range (1,11):
#         print(S,"x",R,"=",S*R)
#     print("-------")

# CODE 25
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# CODE 26
# def cal_pro (a,b,c):
#     pro = a*b*c
#     print(pro)
#     return pro

# pro = cal_pro (5,5,2)
# print ("Pro1",pro)

# pro = cal_pro (5,2,2)
# print ("Pro2",pro)

# pro = cal_pro (5,6,2)
# print ("Pro3",pro)


# CODE 27
# def avg_no (a,b,c):
#     avg = (a+b+c)/2
#     # print(avg)
#     return avg
# ans = print("The avg of 3 no is:",avg_no(45,60,68))

# CODE 28
# def no_check (a):
#     no_check = a
#     if no_check%2==0:
#         print("even")
#     else:
#         print ("odd")
#     # print(no_check)
#     return no_check
# ans = no_check (int(input("enter the no:")))


# CODE 29
# def fact(n):
#     if n == 1:
#         return 1
#     return fact(n-1)*n
# print(fact(int(input("enter no:")))) 

# CODE 30
# def nat_no(n):
#     if n==0:
#         return
#     print(n)
#     nat_no(n-1)
# nat_no(5)

# CODE 30
# def nat_no(n):
#     if n==0:
#         return 0
#     return nat_no(n-1) + n
# sum = nat_no(6)
# print (sum)

# CODE 31
#  PYTHON FILE I/O:
# f = open("shikhass.py","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# CODE 32

#  TO CREATE A NEW DATA OR FILE.
# with open("sample.txt","x") as f:
#     f.close()

# CODE 33

#  TO WRITE OR ADD A NEW DATA ON FILE.
# with open("sample.txt","w") as f:
#     f.write("Hello, This is SR.")

# CODE 34

#  TO MODIFYING OR CHANGE IN A DATA OF FILE.
# with open("sample.txt","a") as f:
#     f.write("\n This is a message from SR_team. \n5521.13.15,sr")

# CODE 35

#  TO READ A CREATED DATA OR FILE.
# with open("sample.txt","r") as f:
#     # print(f.readline(1))
#     # print(f.readline(2))
#     # print(f.read(6))
#     print(f.read())
#     f.close()

# CODE 36
#   TO DELETE A CREATED DATA OR FILE.

# import os

# os.remove("sample.txt")

# CODE 37
# with open("practice.txt","w") as f:
#     f.write("Hi everyone \n")
#     f.write("we are learning File I/O")
#     f.write("\nusing Java \nI like programming in Java.")


# with open("practice.txt","r") as f:
#     file = f.read()
# new_file = file.replace("Java", "Python")
# print(new_file)


# with open("practice.txt","w") as f:
#     f.write(new_file)

# CODE 38