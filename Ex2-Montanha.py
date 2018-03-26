tamanho = int(input('Digite o tamanho do vetor: '))
vetor = [0] * tamanho

######################################
def entre10e40(vet):
  y = []
  for i in vet:
    if i >= 10 and i <= 40:
      y.append(i)
  return y

def posicoesPares(vet):
  w = []
  for i in range(len(vet)):
    if i % 2 == 0:
      w.append(vet[i])
  return w
  
def procuraElemento(vet, elemento):
  z = 0
  for i in range(len(vet)):
    if vet[i] == elemento:
      z = vet[i]
  return z - 1
  
def menorMaior(vet):
  menor = maior = vet[0]
  for i in vet:
    if i < menor:
      menor = i
    if i > maior:
      maior = i
  return menor, maior
  
######################################

for i in range(tamanho):
  vetor[i] = int(input('Digite um numero para a posição'))

elemento = int(input('Digite um número a ser buscado no vetor: '))

y = entre10e40(vetor)
print('\nNúmeros entre 10 e 40: ',y)

w = posicoesPares(vetor)
print('\nPosições pares: ' ,w)

z = procuraElemento(vetor, elemento)
print('\nO elemento que você esta procurando esta na casa: ' ,z)

menor, maior = menorMaior(vetor)
print('\nO menor valor é ', menor, ' e o maior valor é ', maior)