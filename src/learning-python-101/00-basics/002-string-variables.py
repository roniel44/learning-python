my_sentence = "illmatic is the number %d hip-hop album" % 1
more_sentence = "did you know? that %s" % (my_sentence)
print(more_sentence)

am_i_gay = False
print("am i gay? the answer is %r" % (am_i_gay))

sentence1 = "I have a blood of a slave."
sentence2 = "But I have a heart of a king!"
# this concatenation works
print(sentence1 + " ", sentence2)
# this works as well
print(sentence1, " ", sentence2)

# more printing tricks
formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4))
print(formatter % ("Nas", "Jay-Z", "Tupac", "Biggie"))

# new line printing tricks
days_of_the_week = "\nMonday\nTuesday\nWednesday\nThursday\nFriday"
print("Here are the days per new line: ", days_of_the_week)

# this works like the <<EOD tag in PHP
my_paragraph = """
belly of the beast
sweet caliber 45 gun
like a sword into your guts
"""

print(my_paragraph)
