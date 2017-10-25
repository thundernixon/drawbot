def myfunction():
    print "hello from myfunction"
    
def myOtherFunction(arg):
    a = "my letter a"
    print arg * 3
    print a
    
myOtherFunction("hello")

# print a # gives a syntax error, because variable `a` doesn't exist in the global scope

def adder(a,b):
    print "these are the arguments:", a, b
    x = a + b
    return x
    
res = adder(1,2) # cues the function with two arguments, stores as variable

print res # prints "3"

