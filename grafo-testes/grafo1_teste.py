from maior_distancia import maior_distancia

grafo = [
  [0, 1, 1, 0, 0, 0],
  [1, 0, 1, 1, 0, 1],
  [1, 1, 0, 1, 1, 0],
  [0, 1, 1, 0, 1, 1],
  [0, 0, 1, 1, 0, 1],
  [0, 1, 0, 1, 1, 0]
]

distancia = maior_distancia(grafo)
# print("A maior distância no grafo 3 é", distancia)

if distancia == 2:
  print("Teste para o grafo 1 passou, a maior distância é 2.")
else:
  print("Teste para o grafo 2 falhou, esperava distâcia 2 porém calculou", distancia)
