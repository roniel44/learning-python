list = ["abcd", 123, "john", "dignity", 3.14, "000000"]
le_small_list = ["jack", "rose"]
print(list)
# indexing works like in php
print(list[0])  # prints abcd
print(list[3:])  # prints from index onwards
print(list[0:2])  # prints from index 0 to 2
print(le_small_list * 2)  # prints small list twice
print(le_small_list + list)  # prints small list + the list

list[0] = "abcde"
print(list[0])  # prints abcde

numbers_list = [5, 3, 4, 1, 2]
# sorting, this is googable
# only works on all string/numbers list
print(numbers_list)
numbers_list.sort()
print(numbers_list)
# min works as well
print(max(numbers_list))
