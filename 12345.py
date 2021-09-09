w = [1,2,3,4,5,6,7,8,9,0]
q = iter(w)
def nna():
    return next(q)
e = iter(nna,6)
for x in e:
    print(x)
