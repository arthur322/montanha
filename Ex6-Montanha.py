a = [2,4,1,4,6,12,21,6,10,12,23,3]

for i in range(len(a) - 1):
    k = i
    x = a[i]
    for j in range(i + 1, len(a)):
        if a[j] < x:
            k = j
            x = a[k]
    a[k] = a[i]
    a[i] = x
print('Algoritmo principal:')
print(a)

# O algoritmo esta ordenando os valores no vetor, verificando uma casa com as outras
#  próximas para verificar se a casa é a menor. Caso sim, as troca de lugar.
# Uma algoritmo alternativo para melhor implementação seria o código a seguir:

a = [2,4,1,4,6,12,21,6,10,12,23,3]

ordenou = True

while(ordenou):
    ordenou = False
    for i in range(len(a)):
        if i < len(a) - 1 and a[i] > a[i+1]:
                aux = a[i]
                a[i] = a[i+1]
                a[i+1] = aux
                ordenou = True
print('Algoritmo alternativo:')
print(a)