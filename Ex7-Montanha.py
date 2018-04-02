a = [1,3,5,8,4,2,7,0]

ordenou = True

while(ordenou):
    ordenou = False
    for i in range(len(a)):
        if i < len(a) - 1 and a[i] > a[i+1]:
                aux = a[i]
                a[i] = a[i+1]
                a[i+1] = aux
                ordenou = True

print(a)