#Join set1 and set2 into a new set:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#Use | to join two sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

#Join multiple sets with the union() method:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = {4, 5, 6}
set4 = set1.union(set2, set3)
print(set4)

#Join a set with a tuple:   
set1 = {"a", "b" , "c"}
tuple1 = ("d", "e", "f")
set2 = set1.union(tuple1)
print(set2)
