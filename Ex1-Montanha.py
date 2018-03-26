qtd = int(input('Digite quantidade de pessoas entre 0 e 100.'))
sexo = []
altura = []
alturaTotal = 0
countM = 0
countF = 0
somaalturaM = 0
somaalturaF = 0
maior = 0

for i in range(qtd):
  sexo.append(input('Informe o sexo(F ou M):'))
  altura.append(float(input('Informa altura:')))
    
  alturaTotal = alturaTotal + altura[i]
  if i == 0:
    maior = altura
  
  if sexo[i] == 'M':
    countM = countM + 1
    somaalturaM = somaalturaM + altura[i]
  
  if sexo[i] == 'F':
    countF = countF + 1
    somaalturaF = somaalturaF + altura[i]

  if altura > maior:
    maior = altura

mediaPessoas = alturaTotal/qtd
mediaF = somaalturaF/countF
mediaM = somaalturaM/countM


print('Altura média das pessoas: ',mediaPessoas)
print('A maior altura é: ', maior)
print('Altura media das Mulheres: ',mediaF)
print('Altura media dos Homens: ',mediaM)
print('Quantidade de Homens: ',countM)