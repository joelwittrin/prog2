'''
List comprehension
'''

# Shortens loops, structured as '[FUNCTION applied to each ELEMENT in ITERABLE fulfilling CONDITION]
# Creating a list of squares from 1 to 4
lst = [ii**2 for ii in range(1,5)]

# Creating a list of Gamma functions with even numbers up to 9
import math
glist = [math.gamma(ii) for ii in range(1,10) if ii % 2 == 0]

# Creating a nestled list. The inner loop generates elements, the outer the list itself
nestled_lst = [[0 for ii in range(0,2)] for jj in range(0,3)]

def print_lst():
    print(lst)
    print(glist)
    print(nestled_lst)


'''
The lambda function
'''

# Utilize lambda to avoid defining function name, 'f = lambda <ARGUMENT>: <EXPRESSION>'
f = lambda x: x*2

# With two arguments:
f2 = lambda x,y: x+y

# Can generate other functions. Note that double requires an argument and becomes a function
def multiply(n):
    return lambda a: a*n
double = multiply(2)
double(10)

def print_lambda():
    print(f(5))
    print(f2(3, 5))
    print(double(10))

'''
The map function
'''

# Applying a function to an iterable, structured as 'map(f, [1,2,3]) = (f(1), f(2), f(3))'
# Reusing the Gamma:

gmap = list( map(math.gamma, range(1,5)) )

# Combining map with lambda:
maplambda = list( map(lambda x: x*x, range(1,5)) )

# For several arguments, simply add iterables such that 'map(f, iterable1, iterable2...)'. Make sure that f can handle the arguments!
# First iterable is assigned to first variable, though here it doesn't matter
list1 = [1,2,3,4]
list2 = [5,6,7,8]
several = list( map(lambda x, y: x+y, list1, list2) )

# Conversion of a tuple of tuples to a tuple of lists. Iterable tuples -> lists -> stored in tuple
tuple_of_tuples = ( (0,1), (1,2,3), (1,0) )
tuple_of_lists = tuple ( map(list, tuple_of_tuples) )

def print_map():
    print(gmap)
    print(maplambda)
    print(several)
    print(tuple_of_lists)

'''
The functool
'''

# Is used to reduce list down to a single value, often used with map(). Here, (x,y) = (1,-2), where the function is applied to these.
# The result then becomes the new x, and the y is the next element in the iterable, i.e. (x,y) = (-1,3) etc
import functools
lst_reduce = [1, -2, 3, 4]
sum_reduced = functools.reduce(lambda x, y: x+y, lst_reduce)

# Similarily, one can process the argument before applying it. The following code yields the Manhattan norm
manhattan = functools.reduce( lambda x, y: x+y, map(abs, lst_reduce) )

def print_reduce():
    print(sum_reduced)
    print(manhattan)

'''
The filter function
'''

# Filters out if an expression satisfies True / False, e.g. if a number is greater than two. Structured as 'filter(condition, iterable)'
a = [7, 1, -3, 4]
filtered = list( filter(lambda x: x>2, a) )

# The same result can be done through list comprehension and often comes down to personal preference
filtered_lc = [x for x in a if x > 2]

# Filter can be used in more advanced cases where a explicit function is created. Here, filter iterates through the word letter by letter
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö']
    return True if letter in vowels else False

word = 'acetylsalicylsyra'
filtered_vowels = list(filter(filter_vowels, word) )

def print_filtered():
    print(filtered)
    print(filtered_lc)
    print(filtered_vowels)

'''
the zip function
'''

# Used to create iterable of tuples from one or more iterables, structured as 'tuple( zip(iter1, iter2) )= ( (iter1[0], iter2[0]), (iter1[1], iter2[1]) ... )'
# Note that we MUST specify data type, otherwise Python simply returns something like '<zip object at 0x7f8c12345678>' and that we MUST have two iterables!
animals = ['dog', 'cat', 'rabbit']
tuple_of_animals = list( zip(range(3), animals))

# Useful for finding index in a list, e.g. all indices greater than zero. The list is returned as '[ (0, 2), (1, -1), (2, 7), (3, 9) ]'
numbers = [2, -1, 7, 9]
zip_numbers = list( zip(range(len(numbers)), numbers))
filtered_numbers = [ii[0] for ii in zip_numbers if ii[1]>0]

# Several arguments can be used. zip always finishes when the shortest iterable is done!
x = [1, 2, 3, 4, 13, 14]
y = [5, 6, 7, 8]
z = [9, 10, 11, 12, 15]
xyz = list(zip(x,y,z))

def print_zip():
    print(tuple_of_animals)
    print(filtered_numbers)
    print(xyz)

