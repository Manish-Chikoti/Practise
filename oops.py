#cheking for the type 
def hi():
    print("this is working")
#hi()
#print(type(hi))
#return error when we cant operate on 2 different types 
x = "1st"
y = 2.0
#print(x+y)
#Traceback (most recent call last):
#   File "c:\Users\manis\OneDrive\Desktop\ML practise\Practise\oops.py", line 9, in <module>
#     print(x+y)
#           ~^~
# TypeError: can only concatenate str (not "float") to str
#string methods such as upper and lower are shown below 
x = "hello"
y = 1.0
print(x.upper())
#but if we try to use one class's methods for other it doesnt work 
#---->>>>>>>>print(y.upper())
# Traceback (most recent call last):
#   File "c:\Users\manis\OneDrive\Desktop\ML practise\Practise\oops.py", line 20, in <module>
#     print(y.upper())
#           ^^^^^^^
# AttributeError: 'float' object has no attribute 'upper'
#let us build our first own template of a class 
class Kirana:
    def price(self,x):
        print(f"price is {x}")
    
    # def print_price(self,x):
    #     print(price(x))
biscuit = Kirana()
print(biscuit.price(5))
print(type(biscuit))
#observe the output of the type of the biscuit class 
#we can observe it gives the class as ****<class '__main__.Kirana'>***** 
#the above __main__ indicates the module where the class was declared
#__main__ indicated that it was declared in the same file/code module

#one more thing to notice is that for every attribute call or method call of a 
# class instance or in short object , it automatically immeadeately invisibly passes 
# itself as an argument to the method that why "self" is used always while declaring or 
# you can observe this errors 
#  ***** TypeError: Kirana.price() takes 1 positional argument but 2 were given *****


#checkout the attributes in this one 

class Kirana2:
    def __init__(self , x , p):
        self.product_name = x
        self.product_price = p
    def get_price(self,x):
        print(self.product_price)
yeah_boi = Kirana2("Horlics_Sachet",5)
yeah_boi.get_price("Horlics_Sachet")

#bonus learning from the above are that the class have a getter method now 
#Hurray!!
#let us also try out some of the setter methods 

class Kirana3:
    def __init__(self,x,p,d):
        self.price=p
        self.name=x
        self.discount=d
    def get_price(self):
        return self.price
    def set_price(self,x):
        self.price = x
# pindi = Kirana3("maida",30,0)
# print(pindi.get_price())
# pindi.set_price(20)
# print(pindi.get_price())

#that sums for now let me have dinner break and come 
#ah I am back for another session of learning lets rock it today

#now trying to initialize the git commands or git usage from vs code 
