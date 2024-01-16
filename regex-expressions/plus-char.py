import re

batRegex = re.compile(r'Bat(wo)+man') 

batman_mo = batRegex.search('The adventures of Batman')
batwoman_mo = batRegex.search('The adventures of Batwoman')
wowoman_mo = batRegex.search('The adventures of Batwowowowowoman')

# Notice that because of the use of the plus char, the group (wo)+ ,must appear at least 1 or more times.
print(batman_mo == None) 

# Clearly the expresion wowowowoman works. because the group (wo)+ must appears at least 1 time. 
print(wowoman_mo.group())