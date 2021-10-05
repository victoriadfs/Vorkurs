
import csv
import time
with open('text.txt','r') as infile:
    list= infile.readlines()

w = "Aufstockmoeglichkeiten"
h= []
#print(len(w))
for i in range(27):
    h.append(0)
for i in range(len(w)):
    c = w[i]
    if(ord(c)<97):
        h[ord(c)-65] += 1
    else:
        h[ord(c)-97] += 1

for i in range(len(list)):
    nw=h[:]
    if(len(list[i])-1==len(w)):
        pos=True
        a = list[i]
        #print(len(a))
        for k in range (len(w)):
            c = a[k]
            x=0
            if(ord(c)<97):
                x=ord(c)-65
            else:
                x=ord(c)-97
            if(x<0 or x>26):
                print(a)
                pos=False
                break
            nw[x] -= 1
            if(nw[x]<0):
                pos=False
                break
        if(pos== True):
            print(list[i])
