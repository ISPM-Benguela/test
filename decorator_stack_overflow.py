#!bin/usr/python

contador = 0

def contar_acessos(funcao_decorada):
    # não ssabemos quantos parâmetros exostirão na chamada
    # da função funcao_decorada, então receemos *args e **kw
    def nova_func(*args, **kw):
        global contador
        contador += 1
        # e chamamos a função original com os parâmetros recebidos:
        return funcao_decorada(*args, kw)
    # retornamos a função "nova_func" - que só faz
    # icrementar o  contador e retornar o valor da chamada à funcão original
    return nova_func

# agora vamos usar o decorador:
@contar_acessos
def soma(a, b):
    return a + b
nome = input("digite o seu nome: ")
print(nome)
