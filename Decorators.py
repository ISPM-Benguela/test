#!bin/usr/python

class Uppercase(object):

    def __init__(self, f):
        print("Ola mundo, eu sou programador __init__")
        self.f = f

    def __call__(self, *args):
        self.f(args[0].upper())

@Uppercase
def nome(nome):
    print("Nome: %s" % nome)

nome("Fred")

nome = input("Digite o seu nome aqui: ")	
print(nome)

