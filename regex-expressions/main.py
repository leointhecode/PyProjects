import re

# The next one is an example of using regex expressions in order of searching a phone number in a piece od data.

 # we are using and r'' in order of using a raw string to use the commands like \d or \n
#The parenthesis divides the group into 3 subgroups, subgroups that can be accessed with the index 1 (the first subgroup) the n index (the larger subgroup)
# To search a parenthesis you have to use the notation   \(  or  \) 
PhoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')

search_result = PhoneNumberRegex.search('My number is (444-555-6666') 

#print(search_result) # notice that it returns an object, to get the desire information use the .group() (for 1 len returns) 
print(search_result.group(3))


#In order of fynding more complex patterns u can use the pipe characther | when searching for the complement of a prefix, such as;

batRegex = re.compile(r'Bat(mobile|copter|bat)')
mo = batRegex.search('Batcopter lost a wheel')\

print(mo.group())
