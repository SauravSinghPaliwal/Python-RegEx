import re

ptrn = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
s = input().strip()

x = re.match(ptrn,s)
if x:
    print(True)
else:
    print(False)