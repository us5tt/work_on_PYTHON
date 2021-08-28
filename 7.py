simple=[3]
number=3
count=3
while count<=10001:
    number+=2
    simpleNuber=True
    for i in simple:
        if number<i**2: #числа кратные i, начинают высчитывать с i(квадрат)
            break
        else:
            if number%i==0:
                simpleNuber=False
                break
    if simpleNuber==True:
        simple.append(number)
        count+=1
print(simple[-1])