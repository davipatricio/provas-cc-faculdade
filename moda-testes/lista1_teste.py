from moda import moda

lista = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9]
moda_lista = moda(lista)

print("Moda da Lista 1:", moda_lista)

# Teste
if moda_lista == 0:
    print("Os testes da lista 1 passaram. A moda está correta.")
else:
    print("O teste da linha 1 falhou. A moda está incorreta, pois, o esperado era 0.")
