# Avaliação Parcial 2
# Nome: Davi Patricio Gimenes - 2401557
# Matéria: Análise e Projeto de Algoritmos
# Professor: Odair Gabriel
# Curso: Ciência da Computação (3/8)

# Esta função visa encontrar a maior distância entre dois pontos no grafo.
# A complexidade deste algoritmo é O(n^3).

# 1. Para cada vértice, camamos distancias_origem(matriz, i) para calcular as distancia ap artir dele
# 2. Verifica qual é a maior distância nas listas retornadas
# 3. Guarda a maior e todas as distâncias vistas até agora
# 4. Retorna a maior distância encontrada no grafo.
def maior_distancia(matriz):
  max_distancia = 0

  for i in range(len(matriz)):
    distancias = distancias_origem(matriz, i)
    for j in range(len(distancias)):
      if distancias[j] > max_distancia:
        max_distancia = distancias[j]

  return max_distancia

# 1. Criamos três listas auxiliares:
# "visitado" para marcar os vértices já visitados;
# "distancia", para guardar a distância da origem até cada vértice;
# "fila", para simular a fila do busca em largura.
# 2. Coloca o vértice de origem na fila, marca como visitado e define sua distância como 0.
# 3. Realizamos um loop e enquanto houver vértices na fila:
# 3.1 Pega o próximo vértice (atual).
# 3.2 Para cada vizinho do atual, se ainda não foi visitado e há conexão:
# 3.2.a Adiciona o vizinho na fila.
# 3.2.b Marca como visitado.
# 3.2.c Define a distância como distância do atual + 1.
# 4.Retorna a lista distancia, contendo as distâncias da origem até todos os vértices.
def distancias_origem(matriz, origem):
  n = len(matriz)
  visitado = []
  for _ in range(n):
    visitado.append(0)  # 0 = não visitado, 1 = visitado

  distancia = []
  for _ in range(n):
    distancia.append(-1)  # -1 = ainda não alcançado

  fila = []
  fila.append(origem)
  visitado[origem] = 1
  distancia[origem] = 0

  while len(fila) > 0:
    atual = fila[0]
    nova_fila = []
    for i in range(1, len(fila)):
      nova_fila.append(fila[i])
    fila = nova_fila
    for i in range(len(matriz[atual])):
      if matriz[atual][i] == 1 and visitado[i] == 0:
        fila.append(i)
        visitado[i] = 1
        distancia[i] = distancia[atual] + 1

  return distancia