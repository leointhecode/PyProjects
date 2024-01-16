import re

phoneRegex = re.compile(r'd\d\d\-\d\d\d-\d\d\d\d')
#The findall method lets a search in the whole of a text, not delimitated to the first coincidence that it's found.
#The findall method return syntax, it is a list with regular string values, unlike it's cousin the search() method.

#In the case that the Regex has two or more groups in the re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') it will actually return a list of tuples.
print(phoneRegex.findall())