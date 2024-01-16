import re

batRegex = re.compile(r'Bat(wo)?man')

bat_mo = batRegex.search('The adventures of Batwoman') #It also receives Batman

#print(mo.group())

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#If we take out the area (i.e 444) the object will be None, thats why we will use optional group notation (i.e ()?)
phone_mo = phoneRegex.search('My number is (444-555-6666')

#print(phone_mo.group())

# IT RETURNS EITHER WITH THE AREA CODE OR WITHOUT AREA CODE

optional_phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

optional_phone_mo = optional_phoneRegex.search('My number is 444-555-6666')

print(optional_phone_mo.group())

