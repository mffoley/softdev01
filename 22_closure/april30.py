#Maryann Foley
#SoftDev2 pd8
#K22 -- closure
#2019-04-30 

def repeat(x):
    def rree(num):
        return x*num
    return rree

r1=repeat("hello")
r2=repeat("goodbye")
print(r1(5))
print(r2(3))
print(repeat("cool")(3))


def make_counter():
    x=0
    def count():
        nonlocal x
        x+=1
        return(x)
    def curr():
        return(x)
    return count,curr

c1,display1=make_counter()
print(c1())
print(c1())
print(c1())
print("Display count:",str(display1()))

c2,display2=make_counter()
print(c2())
print("Display count:",str(display2()))

'''
def inc(x):
    return x+1

f=inc
print(f)
print(inc)

def inc(x):
    return x+2

print(f)
print(inc)

def adder(a,b):
    return a+b

def caller(c):
    print(c(2,4))
    print(c(3,5))

caller(adder)

def outer(x):
    def contains(l):
        return x in l
    return contains

contains15=outer(15)
print(contains15([1,2,3]))
print(contains15(range(1,20)))
print(contains15([15,25,35]))

print(contains15)
'''
#To create a closure:
#define nested fxn
#nested fxn must refer to var defined in enclosing fxn
#return nested fxn

'''
def outer1():
    x="foo"
    y="boo"
    def inner():
        nonlocal x
        x="bar"
        y="bar"
    inner()
    return x,y

print(outer1())
'''
