import re

S = input()

if re.match('^A[a-z]+C[a-z]+$', S):
    print('AC')
else:
    print('WA')
