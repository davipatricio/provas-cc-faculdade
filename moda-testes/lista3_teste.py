from moda import moda

lista = [(i**3)//1000 for i in range(100, -10, -1)]
moda_lista = moda(lista)

print("Moda da Lista 3:", moda_lista)

# Teste
if moda_lista == 0:
    print("Os testes da lista 3 passaram. A moda está correta.")
else:
    print("O teste da linha 3 falhou. A moda está incorreta, pois, o esperado era 0.")
