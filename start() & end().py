import re

str = input()
substr = input()

pattern = re.compile(substr)
match = pattern.search(str)

if not match: 
    print('(-1, -1)')
    
while match:
    print('({0}, {1})'.format(match.start(), match.end() - 1))
    match = pattern.search(str, match.start() + 1)