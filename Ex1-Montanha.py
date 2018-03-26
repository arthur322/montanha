qtd = int(input('Digite quantidade de pessoas entre 0 e 100.'))
sexo = []
altura = []
alturaTotal = 0
countM = 0
countF = 0
somaalturaM = 0
somaalturaF = 0
mediaF = 0
mediaM = 0
maior = 0

for i in range(qtd):
  sexo.append(input('Informe o sexo(F ou M):'))
  altura.append(float(input('Informa altura:')))
    
  alturaTotal = alturaTotal + altura[i]
  if i == 0:
    maior = altura[i]
  
  if sexo[i].lower() == 'm':
    countM = countM + 1
    somaalturaM = somaalturaM + altura[i]
  
  if sexo[i].lower() == 'f':
    countF = countF + 1
    somaalturaF = somaalturaF + altura[i]

  if altura[i] > maior:
    maior = altura[i]

mediaPessoas = alturaTotal/qtd
if countF > 0:
  mediaF = somaalturaF/countF
if countM > 0:
  mediaM = somaalturaM/countM

print('\n\n')
print('Altura média das pessoas: ',mediaPessoas)
print('A maior altura é: ', maior)
print('Altura media das Mulheres: ',mediaF)
print('Altura media dos Homens: ',mediaM)
print('Quantidade de Homens: ',countM)