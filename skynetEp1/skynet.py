import sys
import math
lien = []
p = []
n, l, e = [int(i) for i in input().split()]
for i in range(l):
    n1, n2 = [int(j) for j in input().split()]
    lien.append([n1, n2])

for i in range(e):
    ei = int(input())
    p.append(ei)

def priority(si, p, lien):
    for i in p:
        test = [si, i]
        test2 = [i, si]
        if test in lien or test2 in lien:
            if test in lien:
                lien.remove(test)
                print(str(test[0]) + " " + str(test[1]))
            elif test2 in lien:
                lien.remove(test2)
                print(str(test2[0]) + " " + str(test2[1]))
            
            return (1)
    return (0)

while True:
    si = int(input())
    if (priority(si, p, lien) == 0):
        print(lien[len(lien) - 1][0], lien[len(lien) - 1][1])
        lien.pop()
