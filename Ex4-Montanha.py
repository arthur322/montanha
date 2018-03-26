tamanho = int(input('Digite um tamanho para o vetor'))
a = [0] * tamanho

for i in range(len(a)):
  a[i] = int(input('Digite um valor para o vetor!'))

repetidos = []
removidos = 0

for i in range(len(a)):
  for j in range(len(a)):
    if a[i] == a[j] and i != j:
      repetidos.append(a[i])
      
for i in range(len(repetidos)):
  if repetidos[i] in a:
    a.remove(repetidos[i])
    removidos += 1

if removidos == 0:
  print('Ok, nenhum elemento repetido!')
else:
  print('Foram removidos ', removidos, ' itens!')