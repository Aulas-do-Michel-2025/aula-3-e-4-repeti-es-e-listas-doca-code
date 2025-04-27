"""
#### Exercício 4 - Lista de organismos

Você recebeu uma lista que contém, para cada organismos detectado numa amostra, uma outra lista contendo a 
quantidade de leituras que esse organismo teve em cada identificador taxonômico.

Obs: Deixei a lista direto no exercício para facilitar. Mas faça o código para descobrir, não coloque a resposta direto!

Por exemplo:

[[100, 200, 300], [1, 99, 10000], [1, 1, 1]].

Eu quero que você identifique o organismo que teve a maior média de leituras entre todos os organismos da lista.

Ao identificar digite a posição em que esse organismo se encontra na lista.

No exemplo acima, você imprimiria:

"O organismo com maior média é o da posição 1 da lista."

Porque o organismo da posição 0 tem média de (100 + 200 + 300) / 3 = 200, o organismo da posição 0
tem média de (1 + 99 + 10000) / 3 = 3366,66 e o da posição 2 tem média de (1 + 1 + 1) / 3 = 1.

Logo o da posição 1 é maior.

------

Exemplo:
lista_de_organismos = [[100, 200, 300], [1, 99, 10000], [1, 1, 1]]

Resposta:
O organismo com maior média é o da posição 1 da lista.

Dica: Utilize mais de um for para resolver o exercício, um para a lista de organismos e um para cada lista. Cuidado com a identação.

O cálculo de média já foi feito em sala e pode ser usado de exemplo.
"""

# Lista
lista_de_organismos = [[50, 50, 50], [125, 99, 12], [19, 91, 42], [40, 189, 0], [1, 0, 0], [100, 100, 70], [99, 12, 12]]

# Fazer a partir daqui

posicao_organismo = 1
maior_organismo = 0
maior_media = 0
for organismo in lista_de_organismos:
  total_leitura_organismo = 0
  media_leitura_organismo = 0
  posicao_organismo +=1
  for leitura in organismo:
    total_leitura_organismo += leitura
  media_leitura_organismo = total_leitura_organismo/len(organismo)
  if media_leitura_organismo > maior_media:
    maior_media = media_leitura_organismo
    maior_organismo = posicao_organismo
  #print(f'Para o organismo: {posicao_organismo} o total leitura é: {total_leitura_organismo} e Media é: {media_leitura_organismo}')
print(f'O organismo com maior média é o da posição {maior_organismo} da lista.')
