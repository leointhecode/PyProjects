import re

#Because of the star char, this can apper zero or more times.
batRegex = re.compile(r'Bat(wo)*man') 

#It will return the expected value on the 3 cases, because of the condition of being able to catch an expresision zero or more times
#the var bat_wowoman works.
batman_mo = batRegex.search('The adventures of Batman')
batwoman_mo = batRegex.search('The adventures of Batwoman')
bat_wowoman = batRegex.search('The adventures of Batwowowowowoman')

print(bat_wowoman.group())