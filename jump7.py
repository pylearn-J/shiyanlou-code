a=0
while a<=99:
    a+=1
    if a%7==0 or a%10==7 or a//10==7:
        continue
    else:
        print(a)

