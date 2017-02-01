import re
str1 = '((((((((((((((2, 3)))))))))))))'


a = str1.count('(')
b = str1.count(')')

print ("number of '(' is: ", a)
print ("number of ')' is: ", b)
print ("")

if a == b:
    print ("We are happy, because we don't write a code")
else:
    print ("We aren't happy, because we must write a code")
    print ("")

    list_of_all_digits = re.findall('\d', str1)

    first_dig, second_dig = list_of_all_digits    
    
    index_1 = int(str1.index(first_dig))
    
    first_slicing = str1[0:index_1]
    
    second_slicing = first_slicing[::-1]
    
    second_slicing = second_slicing.replace('(', ')')
     
    my_correct_output = first_slicing + first_dig + ', ' + second_dig + second_slicing
    print (my_correct_output)
    print ("")
    
    a2 = my_correct_output.count('(')
    b2 = my_correct_output.count(')')

    print ("number of '(' is: ", a2)
    print ("number of ')' is: ", b2)
