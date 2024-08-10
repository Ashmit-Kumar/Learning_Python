d={}
d["Name"]="Ashmit"
# d["age"]=20
# print(d)

d.setdefault('city',"Kanpur")
# d.update(Pin=202020)
d.update({"College":"LIT","Status":"Unemployed"})
# print(d)

# print(d.keys())
# print(d.values())
# print(d.items())

# c=dict(sorted(d.items()))


# Using lambda expression
sorted1=dict(sorted(d.items(),key=lambda item:item[1]))
print(sorted1)
# my_dict = {'banana': 3, 'apple': 2, 'cherry': 5}

# # Sort by values in descending order
# sorted_by_values_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

# print(sorted_by_values_desc)
# Output: {'cherry': 5, 'banana': 3, 'apple': 2}


# print(c)
