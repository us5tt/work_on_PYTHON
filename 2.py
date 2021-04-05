#eyler_2

dict = {}
def fib(x):
    if x in dict:
        return dict[x]
    if x==1:
        f = 1
    elif x==2:
        f = 2
    else:
        f = fib(x-1) + fib(x-2)
    dict[x]=f
    return f

i = 1
su = 0
fin = 1

while fin < 4000000:
    fin = fib(i)
    if fin%2 == 0:
        su += fib(i)
    i+=1

print (su)