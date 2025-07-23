lst = ['a', 'b', 'c']

for i, j in enumerate(lst):
    print(i+1, j) 

print(''.join(lst)) 


def check_ten_sum(n1,n2):
    # Code Here
    if (n1+n2)==10:
        return True
    return n1+n2

# print(check_ten_sum(6, 4)) 

def first_upper(mystring):
    return mystring[0].upper()

# print(first_upper())
    

def seq_check(nums):
    s = ""
    for i in nums:
        s+= str(i)
    if "123" in s:
        return True
    else:
        return False 

# print(seq_check([0,2,3,4,5])) 



name = 'This is a global name'

def greet():
    # Enclosing function
    name = 'Sammy'

    def hello():
        print('Hello '+name)

    hello()

greet()


print(name)


