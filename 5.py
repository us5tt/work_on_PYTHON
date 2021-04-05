i=2520 #Делимость на 20
c=False
r=(3,4,6,7,8,9,11,12,13,14,15,16,17,18,19)
while c is False:
    str(i)
    for j in r:
        if i%j==0:
            c=True
            continue
        else:
            c=False
            break
    i+=10 #Только четные

print(i-10)