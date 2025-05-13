from moda import moda

lista = [i//10 for i in range(100, -10, -1)] + [10,11,12,13,14,5,16,17,18,19]
moda_lista = moda(lista)

print("Moda da Lista 2:", moda_lista)

# Teste
if moda_lista == 5 or moda_lista == 9:
    print("Os testes da lista 2 passaram. A moda está correta (5 ou 9).")
else:
    print("O teste da linha 2 falhou. A moda está incorreta, pois, o esperado era 5 ou 9.")
