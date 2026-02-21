d = [5 , 3, 7, 10, 32] #list 
iter (d) #iterable object
it = iter(d) #iterator object
print(next(it)) #5
print(next(it)) #3
print(next(it)) #7
print(next(it)) #10  
print(next(it)) #32
print(next(it)) #StopIteration error

mystr = "banana" #string is also an iterable object
myit = iter(mystr) #iterator object

print(next(myit)) #b
print(next(myit)) #a
print(next(myit)) #n
print(next(myit)) #a
print(next(myit)) #n  
print(next(myit)) #StopIteration error

range (0, 5) #range is also an iterable object
iter= iter(range( 0 ,5)) #iterator object
print(next(iter)) #0
print(next(iter)) #1
print(next(iter)) #2
print(next(iter)) #3
print(next(iter)) #4
print(next(iter)) #StopIteration error

class MyNumbers:   
    def iter(self):
        self.a = 1
        return self

    def next(self):
        if self.a > 5:            # остановка после 5
            raise StopIteration
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#Generators 
def mygen(): #generator function
    n = 1 #generator object is created but the function is not yet executed
    print('This is printed first') #the function is executed until the first yield statement
    yield n #the function is paused and the value of n is returned to the caller

    n += 1 
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

a = mygen() #generator object is created but the function is not yet executed
print(next(a)) #This is printed first 1
print(next(a)) #This is printed second 2
print(next(a)) #This is printed at last 3

my_generator = (num for num in range (1, 1000)) #generator expression
print (sys.getsizeof(my_generator)) #size of generator object in bytes
for num in my_generator: #iterating through the generator object
    print(num) #1
    