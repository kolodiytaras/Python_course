import re
lst1 = [1, [2, 3], 4, [[6, 7, [5], [[[6, 8]]]]]]

a = str(lst1).count('[')
b = str(lst1).count(']')

print ("number of '[' is: ", a)
print ("number of ']' is: ", b)
print ("")

if a == b:
    print ("We are happy, because we don't write a code")
