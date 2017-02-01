import re
import math
str1 = '{[([[[(} 2, 5 {]]](()'

a = str1.count('(')
b = str1.count(')')
c = str1.count('{')
d = str1.count('}')
e = str1.count('[')
f = str1.count(']')

print ("number of '(' is: ", a)
print ("number of ')' is: ", b)
print ("number of '{' is: ", c)
print ("number of '}' is: ", d)
print ("number of '[' is: ", e)
print ("number of ']' is: ", f)
print ("")
   
if a==b and c==d and e==f:
    print ("We are happy, because we don't write a code")
else:
    for i in str1:
        a = str1.count('(')
        b = str1.count(')')    
        if a > b:
            str1 = str1 + ')'
        if b > a:
            str1 = str1 + '('
        c = str1.count('{')
        d = str1.count('}')   
        if c > d:
            str1 = str1 + '}'
        if d > c:   
            str1 = str1 + '{'
        e = str1.count('[')
        f = str1.count(']')        
        if e > f:
            str1 = str1 + ']'
        if f > e:   
            str1 = str1 + '['    
        
    print ("correct_output: ", str1)
    print ("")
    
    a = str1.count('(')
    b = str1.count(')')
    c = str1.count('{')
    d = str1.count('}')
    e = str1.count('[')
    f = str1.count(']')
            
    print ("number of '(' is: ", a)
    print ("number of ')' is: ", b)
    print ("number of '{' is: ", c)
    print ("number of '}' is: ", d)
    print ("number of '[' is: ", e)
    print ("number of ']' is: ", f)
