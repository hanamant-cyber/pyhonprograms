# def show(n):
#      if(n == 99):
#           return
#      print(n)
#      show(n+1)
# show(1)
# factorial in recursion

# def fact(n):
#     if(n == 1 or n==0):
#         return 1
#     return fact(n-1) * n
     
      
# print(fact(4))  

def num_sum(n):
    if(n == 0):
        return 0
    return num_sum(n-1) + n
sum = num_sum(8) 
print(sum)   
#     sum = a+b
#     print(sum)
# num(2,3)    

     