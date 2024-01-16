import re

#If we want to only find in the text a certain number of repetitions of the group, we must use the curly braces {}
batRegex = re.compile(r'Bat((wo)?){5}man') 

#Because of the type the expression if the str has more than 5 (wo) it will return None, nevrtheless it returns the output with 5 or less

#As a note you can create a range of expected repetitions by using the syntax {i,n} where i is the min and n the max number of iterations
#If you leave the second param empty, it would mean i iterations or more (i.e {i,})
batman_mo = batRegex.search('The adventures of Batman')
batwoman_mo = batRegex.search('The adventures of Batwoman')
bat_wowoman = batRegex.search('The adventures of Batwowowowoman')

print(bat_wowoman.group())

#By default python will do a greedy match, which means that it will find the largest str possible that matches the pattern
numRegex = re.compile(r'\d{3,5}')
greedy_mo = numRegex.search('0123456789')

#It will return the maximum, in this case is 5, (max no. of iterations)
print(greedy_mo.group())

#A question mark char after a pattern like this with repetitions and curly braces, it won't mean an optional group, it will rather mean to make a non greedy search 
nonGreedy_numRegex = re.compile(r'\d{3,5}?')
nonGreedy_mo = nonGreedy_numRegex.search('0123456789')

print(f'non greedy {nonGreedy_mo.group()}')

