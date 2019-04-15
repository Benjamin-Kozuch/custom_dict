# Custom Hash Map with amortized constant lookup

The following repo holds a custom Hash Map written in python without using any hashmap python primitives (like the builtin dict class)


# Approach

My approach was to create a class that stored a list of elements set at an initial size. Each element would store a 2 part tuple holding the key and value of that specific mapping: 

[(key, value), None, None, ... ,(key, value), (key, value), None]

The initial storage list starts off with every element equal to None and those Nones are replaced with the 2 part tuple as more keys and values are added.

## Insert

In order to insert a key value pair into the storage you first have to take a hash of the key (using pythons builtin `hash()` function).
Then get the remainder after dividing that hash value by the length of the table. That remainder will be the initial attempt of which position to insert that key, value tuple into our storage list. 

If that position has a value of None or a tuple already exists there whose key is the same as the key we are trying insert, then we will insert our key, value tuple in that spot. 

If that spot is already taken by a tuple (whose key is different that the key we are trying to insert) then we will jump over to the next position in the list and check for the same things and keep jumping until we find the proper position for our new element. This is called linear probing.

In the event that we jumped on over to ALL positions from our list (from the position we started from all the way to starting_position - 1) then that means that there are no more available positions and we have to resize our list.

In that scenario we create a new list with twice the size, and re-hash all our previous elements into the new bigger list (whose positions would change since we are dividing by a new list size in our modular operation).

Any value that can be hashed using `hash()` can be a valid key in this Dict (even a tuple can be a proper key)

Examples:

(upon initializing the Dict)

my_dict = Dict(('x', 1))

(after initializing the Dict)

my_dict['x'] = 2
my_dict['y'] = 3
my_dict[(3,4,5)] = 4

## Lookup

Looking up a value (`print(my_dict['x'])`) involves taking the hash of the passed in key. Then take the remainder of that element after dividing by the storage size. Check that position in the list. If that element has the same key as the one we are looking up, then return the value associated with that key. If not, then keep jumping and jumping to the next element until we find a key that matches the one we are looking up and then return that value associated with that key.

# Run Tests

No need to install any libraries. Just have Python 3 installed

`$ python custom_dict_test.py` 





