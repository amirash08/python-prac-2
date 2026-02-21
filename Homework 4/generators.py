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

