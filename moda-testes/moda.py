# Avaliação Parcial 2
# Nome: Davi Patricio Gimenes - 2401557
# Matéria: Análise e Projeto de Algoritmos
# Professor: Odair Gabriel
# Curso: Ciência da Computação (3/8)

# Esta função visa encontrar o valor que mais se repete numa lista.
# A complexiadade deste algoritmo é O(n^2).

# 1. Inicializa maior_freq como 0 e moda_num como None.
# 2. Itera sobre cada elemento da lista com um loop externo.
# 3. Para cada elemento, utiliza um loop interno para contar quantas vezes esse elemento aparece na lista (freq_elem_atual).
# 4. Compara a frequência do elemento atual (freq_elem_atual) com a maior frequência encontrada até então (maior_freq).
# 5. Se a frequência atual for maior, atualiza maior_freq com essa nova frequência e moda_num com o elemento atual.
# 6. Ao final das iterações, retorna o número que teve a maior frequência encontrada (moda_num), que é a moda da lista.
def moda(lista):
  maior_freq = 0
  moda_num = None

  # Itera sobre cada elemento da lista (loop externo)
  for i in range(len(lista)):
    atual = lista[i]
    freq_elem_atual = 0

    # Conta a frequência do elemento atual (loop interno)
    for j in range(len(lista)):
      if lista[j] == atual:
        # Incrementa o contador
        freq_elem_atual += 1

    # Se a frequência atual for maior que a máxima encontrada até agora
    if freq_elem_atual > maior_freq:
      maior_freq = freq_elem_atual
      moda_num = atual

  return moda_num
