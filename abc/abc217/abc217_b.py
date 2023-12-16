S1 = input()
S2 = input()
S3 = input()

result = {'ABC' , 'ARC' , 'AGC' , 'AHC'}
result.remove(S1)
result.remove(S2)
result.remove(S3)
print(*result)
