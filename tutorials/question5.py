a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
i =0
j =0
end = len(a)
end2 = len(b)

while i<end:
    if a[i] in b:
        if a[i] not in c:
          c.append(a[i])
    i += 1

while j<end2:
    if b[j] in a:
        if b[j] not in c:
          c.append(b[j])
    j+= 1



print(c)