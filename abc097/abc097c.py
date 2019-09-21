import sys
s = input()
k = int(input())
alphabets = list(sorted(set(s)))
if k == 1:
  print(alphabets[0])
  sys.exit()

def l2s(list, alphabets):
  return ''.join(alphabets[i] for i in list)

j = 1
list = [0, 0]
while True:
  t = l2s(list, alphabets)
  if s.find(t) != -1:
    j += 1
    if k == j:
      print(t)
      sys.exit()
    list.append(0)
  else:
   list[-1] += 1
   while list[-1] == len(alphabets):
     list.pop()
     list[-1] += 1
