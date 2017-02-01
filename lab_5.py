import re
lst1 = [1, [2, 3], 4, [[6, 7]]]

str1 = str(lst1)

list_of_all_digits = re.findall('\d', str1)

new_lst= list(map(int, list_of_all_digits))

print ("correct_output: ", sorted(new_lst))
