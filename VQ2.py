# a list is a sequence of items 
# 1D lists like a single row or column in excel 
#declare a list using [] and a comma seperated list of values 



#---------- -4, -3, -2, -1
#------------0, 1,  2,   3
list_ints = [100, 1 , 10 ,20]
# there are unique indexes for each element in the list
# 0-based, first at 0 and the last element is at n-1
# n is number of elements in the list 

print(list_ints[0])
print(list_ints[-4])

#types can be mixed in a list

list_numbers = [0, 0.0 , 1 , 1.0, -2]
print(list_numbers)
print(type(list_numbers))
#lists are mutable (they can be changed)
list_numbers[0] = "hello"
print(list_numbers)

#use len() to find out how many elments in a list
print(len(list_numbers))
list_numbers.append("another element")
#print our the last element in the list
print(list_numbers[len(list_numbers)-1])

#we can declare an empty list
empty_list = []
print(len(empty_list))

#we can have lists of lists (2D or ND)
nested_list = [[0,1], [2], [3], [4,5], []]
print(len(nested_list))
print(len(nested_list[0]))

#looping through list items 
candies = ["twix", "reeses", "oreos", "snickers"]
print(candies)
for candy in candies:
    print(candy)

i = 0
while i < len(candies):
    print(i, candies[i])
    i += 1

i = 0 
for i in range(len(candies)):
    print(i, candies[i])

#common list operators
#list concatenation...adding 2 lists together 
print(candies)
candies += ["m&ms", "starburst"]
print(candies)
#list repetition...repeating elements in a list
bag_o_candies = 5 * ["twix", "snickers"]
print(bag_o_candies)
#list slicing
print(candies[1:3]) # : is the slice operator. Start value is inclusive and end value is exclusive 
#end index is exclusive
#if you ever need a copy of a list you can use : with no start or end indices 
copy_of_candies = candies[:]
copy_of_candies[0] = "TWIX"
print(copy_of_candies)
print(candies)

#list methods
#candies.