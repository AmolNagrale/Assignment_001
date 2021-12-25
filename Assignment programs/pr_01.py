s = 'Learnig python is very easy'

# output = easy very is python Learning

s1 = s.split()
l1 = []
i = len(s1)-1
while i>=0:
    l1.append(s1[i])
    i-=1
output = ' '.join(l1)
print(output)
   