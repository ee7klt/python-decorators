def foo(x):
	print locals()

foo(1)


# function arguments and parameters
# function defined with one paramter named and one positional
def foo(x, y=0):
	return (x - y)
# passing both parameters positionally
(foo(3,1))
foo(3)
#foo()
# passing both parameters named. order does not matter since named
(foo(y=1,x=3))


def outer():
	x = 100
	def inner ():
		print x
	inner()

print(outer())


issubclass(int, object)

def foo():
	pass

issubclass(foo.__class__, object)

def add(x,y):
	x+y

def sub(x,y):
	x-y

def apply(func, x, y):
	return func(x,y)

print(apply(add, 2 ,1))
print(apply(sub, 2, 1))
