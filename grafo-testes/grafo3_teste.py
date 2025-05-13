from maior_distancia import maior_distancia

grafo = [
  [0, 1, 0, 0, 0, 0],
  [1, 0, 1, 1, 0, 1],
  [0, 1, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1],
  [0, 1, 0, 0, 1, 0]
]

distancia = maior_distancia(grafo)
# print("A maior distância no grafo 1 é", distancia)

if distancia == 3:
  print("Teste para o grafo 3 passou, a maior distância é 3.")
else:
  print("Teste para o grafo 3 falhou, esperava distâcia 3 porém calculou", distancia)
