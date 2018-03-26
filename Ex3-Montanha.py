tamanho = int(input('Digite um tamanho para os vetores'))
a = [0] * tamanho
b = [0] * tamanho

for i in range(len(a)):
  a[i] = int(input('Digite o valor para o vetor A'))

for i in range(len(b)):
  b[i] = int(input('Digite o valor para o vetor B'))

c = []

for i in range(tamanho):
  c.append(a[i])
  c.append(b[i])
  
  
print(c)