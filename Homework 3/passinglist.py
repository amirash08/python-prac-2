def sum_list(nums):
    return sum(nums)
print(sum_list([1,2,3,4]))

def count_letters(text):
    return len(text)
print(count_letters("Python"))

def get_city(user):
    return user["city"]
print(get_city({"name"; "Amir"; "city": "Almaty"}))

def describe(name, scores):
    return f"{name} has {len(scores)} scores"
print(describe("Amir", [90, 80, 120]))
