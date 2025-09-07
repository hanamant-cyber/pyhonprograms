# object orinted programing langauge

# class Student:
#     college_name = "muncipal"
#     name = "dffg"

#     def __init__(self, fullname, marks):
#         self.name = fullname
#         self.marks = marks
#     def welcome(self):
#         print("welcome student,",self.name)

#         # print("adding new student in database..")
#     def get_marks(self):
#         return self.marks

# s1  = Student("karan", 88)
# s1.welcome()
# print(s1.get_marks)
# s3 = Student("hanamant", 44)
# s2 = Student("arjun", 99)
# print(s2.name, s2.marks)
# print(s1.college_name)
# print(s1.name)
# print(s1.name)    

# class Car:
#     color = "blue"
#     brand = "lamborgine"
# Car1= Car()
# print(Car1.color)
# print(Car1.brand)

# 
# Abstraction conepet


# class car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.cluth = True
#         self.acc = True
#         print("car started..") 
# car1 = car()
# car1.start()            

# encapslution


# crete accont class with 2 attributes-balance and accont no 
# crete methods for debit aredit nd printing the blnce

# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc

#         #debit method
#     def debit(self, amount):
#             self.balance -= amount
#             print("Rs.", amount, "was debited")
#             print("total balance = ", self.get_balance())

#     def credit(self, amount):
#             self.balance += amount
#             print("rs.", amount, "was credit") 
#             print("total balance = ", self.get_balance())

#     def get_balance(self):
#             return self.balance      

# acc1 = Account(10000 , 12345)  
# acc1.debit(100) 
# acc1.credit(1000)


# class student:
#     def __init__(self, name):
#         self.name = name
# s1=student("hanamnt")
# print(s1.name)
# del s1.name
 


# class account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass)



# acc1 = account("1123", "jfklj")

# print(acc1.acc_no)
# print(acc1.reset_pass)

# class person:
#     __name = "anonymous"

#     def __hello(self):
#      print("helo person!")

#     def welcome(self):
#      self.__hello()

# p1 = person()

# print(p1.welcome())

# class Car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class toyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class fortuner(toyotaCar):
#     def __init__(self, type):
#         self.type = type        

# # car1 = toyotaCar("fortuner")
# # car2 = toyotaCar("prius")  
# # print(car1.start())   
# car1 = fortuner("diesel")
# car1.start()  
# 
# multiple inheritance 
# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A, B):
#     varC = "welcome to class C"

# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

# super mthod
# class Car:
#     def __init__(self, type):
#         self.type = type
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class toyotaCar(Car):
#     def __init__(self, name, type):
#         self.name = name
#         super().__init__(type)
#         super().start()

# car1 = toyotaCar("prius", "electric")
# print(car1.type)            
          


    #property method
# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math

#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"


# stu1 = Student(98, 97, 99)
# print(stu1.percentage)

# stu1.phy = 77
# print(stu1.percentage)
print("hello world")
print("hanamant")
