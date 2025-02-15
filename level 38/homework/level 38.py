# 2) Tuple Indexing & Slicing: Create a tuple with at least 5 elements and extract the second, last, and a slice of the middle three elements.
tuple1 = (15 , "Goa" , 60.2 , 3.14 , "laptop")
print(tuple1[1])
print(tuple1[4])
print(tuple1[1:4])
# 3) Tuple Immutability: Try to modify an element in a tuple and observe what happens.
# tuple2 = (1 , 2 , 4 , 7 , 3.14)
# tuple2[2] = 100
# print(tuple2)
# error
# 4) Tuple Packing & Unpacking: Create a tuple with multiple values, unpack them into separate variables, and print each variable.
tuple3 = (1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9)
year1,year2,year3,year4,year5,year6,year7,year8,year9 = tuple3
print("year1: " , year1)
print("year2: " , year2)
print("year3: " , year3)
print("year4: " , year4)
print("year5: " , year5)
print("year6: " , year6)
print("year7: " , year7)
print("year8: " , year8)
print("year9: " , year9)
# 5) Tuple Methods: Use the .count() and .index() methods on a tuple containing repeated elements to count occurrences and find the first occurrence of a specific value.
tuple4 = (1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 8 , 8 , 9)
count = tuple4.count(8)
print(count)
index = tuple4.index(8)
print(index)
# 6) Set Creation & Basic Operations: Create a set with at least five elements, add a new element, remove an existing one, and check if a specific value is present in the set.
set1 = {"nika" , "samkharadze" , 14 , "goa" , 3.14 , 5}
set1.add("nikga")
print(set1)
set1.remove("goa")
print(set1)
# 7) Set Union & Intersection: Create two sets with some common elements and perform union, intersection, and difference operations.
set2 = {1 , 2 , 3 , 4 , 5 , 5}
set3 = {6 , 7 , 8 , 9 , 10 , 11}
union_set = set2.union(set3)
print(union_set)
difference_set = set2.difference(set3)
print(difference_set)
# 8) Removing Duplicates: Convert a list with duplicate elements into a set to remove duplicates and then convert it back to a list.
def no_duplicates(user_list):
    return list(set(user_list))

print(no_duplicates([4 , 4 , 7 , 9]))
print(no_duplicates([1 , 2 , 1 , 3]))
print(no_duplicates([2 , 2 , 5 , 1]))
print(no_duplicates([3 , 3 , 4 , 5]))