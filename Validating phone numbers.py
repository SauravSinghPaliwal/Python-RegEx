import re
N = int(input())
for k in range(N):
    pat = r'^[789]\d{9}$'
    print ( 'YES' if re.match(pat,input()) else 'NO')