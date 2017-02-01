import re
incorrect_input = '(({({[1, 3])})'
correct_output = '(({({[1, 3]})}))'

a = incorrect_input.count('(')
b = incorrect_input.count(')')
c = incorrect_input.count('{')
d = incorrect_input.count('}')
e = incorrect_input.count('[')
f = incorrect_input.count(']')

print ("number of '(' is: ", a)
print ("number of ')' is: ", b)
print ("number of '{' is: ", a)
print ("number of '}' is: ", b)
print ("number of '[' is: ", a)
print ("number of ']' is: ", b)
print ("")

if a==b and c==d and e==f:
    print ("We are happy, because we don't write a code")
else:
    print ("We aren't happy, because we must write a code")
    print ("")
    
    list_of_all_digits = re.findall('\d', incorrect_input)

    first_dig, second_dig = list_of_all_digits
    
    index_1 = int(incorrect_input.index(first_dig))
    
    first_slicing = incorrect_input[0:index_1]
    
    second_slicing = first_slicing[::-1]
    
    second_slicing = second_slicing.replace('[', ']')

    second_slicing = second_slicing.replace('{', '}')

    second_slicing = second_slicing.replace('(', ')')
    
    my_correct_output = first_slicing + first_dig + ', ' + second_dig + second_slicing
    print ("my_correct_output is: ", my_correct_output)
    print ("")
    
    a2 = my_correct_output.count('(')
    b2 = my_correct_output.count(')')
    c2 = my_correct_output.count('{')
    d2 = my_correct_output.count('}')
    e2 = my_correct_output.count('[')
    f2 = my_correct_output.count(']')
    
    print ("number of '(' is: ", a2)
    print ("number of ')' is: ", b2)
    print ("number of '{' is: ", a2)
    print ("number of '}' is: ", b2)
    print ("number of '[' is: ", a2)
    print ("number of ']' is: ", b2)    