my_set = {1,2,3,3}
print(my_set)


my_set = set([4,5,5,6])
print(my_set)

set1={1,2,3}
set2={3,4,5}
#Union
union_result_method = set1.union(set2)
union_result_operator = set1 | set2
print("Union of set1 and set2 using union method:", union_result_method)
print("Union of set1 and set2 using union operator:", union_result_operator)

#Intersection
intersection_method = set1.intersection(set2)
intersection_operator = set1 & set2
print("Intersection of set1 and set2 using intersection operator:", intersection_method)
print("Intersection of set1 and set2 using intersection operator:", intersection_operator)

#Difference
difference_method = set1.difference(set2)
difference_operator = set1 - set2
print("Difference of set1 and set2 using difference method:", difference_method)
print("Difference of set1 and set2 using difference operator:", difference_method)

symmetric_differenc_method = set1.symmetric_difference(set2)
print("Symmetric difference of set1 and set2 using symmetric difference method:", symmetric_difference_method)
print("Symmetric difference of set1 and set2 using symmetric difference operator:", symmetric_difference_operator)

#Set method
my_set = {1,2,3}

my_set.add(7)
print(my_set)

my_set.remove(7)
print(my_set)

my_set.discard(8)
print(my_set)

my_set.clear()
print(my_set)

#IN Operator

colors = {"red","green","blue"}
color = "green"

print(color in colors)
print(color not in colors)
