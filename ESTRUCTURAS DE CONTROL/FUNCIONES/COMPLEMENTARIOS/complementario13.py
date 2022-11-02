"""def proximo_primo(num):
    cont=0
    while cont!=2:
        cont=0
        for i in range(1,num):
            if num%(i+1)==0:
                cont+=1
        num+=1
    else:
        sal=num-1

    return sal"""




num=4
cont=0
for i in range(1,num):
    if num%(i)==0:
        cont+=1
    print(i)

print('--', cont)