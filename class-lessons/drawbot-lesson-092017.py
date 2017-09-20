a = 20
b = 20


fill(0.5,0.51,.01)

for i in range(20):
    fill(random(),random(),random())
    rect(+(i*randint(20,30)), +(i*randint(20,30)), 200*randint(1,3), 200*randint(1,3))
    
    
if 3:
    print "yes"
    # non-zero numbers or strings are true
    
if 0:
    print "zero"
    # false
    
if "":
    print "empty string"
    # false
    
if True:
    print "True"
    # True (and False) have capitals
    

if 2 < 5:
    print "yup"
    # 2 < 5 can be run anywhere, and the True/False value can be referenced

if a is not None:
    print "yes"
    
if a != b:
  print "a doesn't equal b"
  
list = [12, 34, 123, 232, "hey look a string"]

print list[1] # prints 34
print len(list) # prints 5, the "length" of the list

print list[-1] # prints last item
print list[-2] # prints second-to-last item
print list[len(list) - 1] # longer form of list[-1]

print len("abc") # prints 3

list.append("a new item")
print list # [12, 34, 123, 232, 'hey look a string', 'a new item']



residents = ["carlos", "stephen", "sean"]

for roommate in residents:
  print roommate
  
  
for item in "abcde":
    print item
    
## Ranges

print range(5)

for i in range(5):
    fill(0,0,0)
    stroke(1,1,1)
    strokeWidth(10)
    x = i * 100 + 50
    rect(x, 50,50,50)