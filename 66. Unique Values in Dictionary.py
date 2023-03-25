# 66. Write a Python program to Extract Unique values dictionary values

dict1 = {'k1': 1, 'k2': 1, 'k3': 'hello', 'k4': 'hello', 'k5':1234}
print("Unique Values : {}".format({i for i in dict1.values()}))

# print("All Keys of Dictionary : {}".format({i for i in dict1.keys()}))