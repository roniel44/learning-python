list = ["abcd", 123, "john", "dignity", 3.14, "000000"]
le_small_list = ["jack", "rose"]
print (list)
#indexing works like in php
print (list[0]) # prints abcd
print (list[3:]) #prints from index onwards
print (list[0:2]) #prints from index 0 to 2
print (le_small_list * 2) #prints small list twice
print (le_small_list + list) #prints small list + the list

list[0] = "abcde"
print (list[0]) # prints abcde