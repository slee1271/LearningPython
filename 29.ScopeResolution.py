# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) local -> enclose -> gloabl -> built-in. Code will go in that order of operations (LEGB)


y = 10 # global scope

#function within a function is allowed in python 
def func1():
    a = 1 # local variable and cant be accessed from the outside
    print(a)
    x = 5 # enclosed variable
    def func2():
        # x = 2 # would be local but when commented out "x = 5" is called an enclosed variable
        print(x)
        print(y)
    func2()

func1()

from math import e # "e" is built-in so it will be the last in the global scope
e = 3 

def func3():
    print(e)
    
func3() #if "e" is defined as a global scope it will be used before the math imported "e"