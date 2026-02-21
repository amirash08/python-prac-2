nums = [1,2,3]
res = list(map(lambda x: x * 2, nums))
print(res)

nums = [2,4,6]
res = list(map(lambda x: x**2, nums))
print (res)

words = ["hi", "python" , "ok"] 
res = list(map(lambda w: w.upper(),words))
print(res)

user = [{"name": "Ann"}]
res = list(map(lambda u: u{"name"}))
print (res) 
