import re

description = list(filter(None, re.split(' |#', 'Tret #wre#re sdsd\nffsf')))
a = [re.split(r'\n|\s', i)[0] for i in description]
print(a)
