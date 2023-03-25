# 69. Write a Python program to convert key-values list to flat dictionary

test_dict = {'month' : [1, 2, 3], 'name' : ['Jan', 'Feb', 'March']}

# Using dict() + zip() to convert key-values list to flat dictionary
res = dict(zip(test_dict['month'], test_dict['name']))
# print("Flattened dictionary : {}".format(res))
print("Flattened dictionary : "+str(res))