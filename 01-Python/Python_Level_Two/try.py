# class Animal:
#     def __init__(self):
#         print("animal")

#     def report(self, cnt):
#         self.cnt = cnt
#         print("report", cnt) 


# class Dog(Animal):
#     def __init__(self, a, b):
#         self.a= a
#         self.b = b
#         print("dog")
    
#     def __repr__(self):
#         # return super().__repr__()
#         return f"a: {self.a} , b: {self.b}"

#     def report(self, cnt):
#         print("reporting..", cnt)

    
# a = Animal()
# a.report(45)

# d= Dog(30, 40) 
# d.report(4)
# print(d) 



# def f1(name = "rh"):
#     print("f1")

#     def f2():
#         print("f2")

#     def f3():
#         print("f3") 
    
#     if name == "rhf":
#         return f2
#     else:
#         return f3
    
# x = f1()
# x()
     


def hello():
    return "Hellooo"

def other(fun):
    print("Other")

    print(fun()) 

other(hello)

    


