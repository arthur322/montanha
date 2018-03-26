tamanho = int(input('Digite o tamanho da sequência: '))

fabricio = [0] * tamanho

if tamanho > 1:
  fabricio[0] = 1
  fabricio[1] = 1

  for i in range(2,len(fabricio)):
    fabricio[i] = fabricio[i-1] + fabricio[i-2]
  
print(fabricio)