#!/usr/bin/env python

arq = open('/tmp/lista.txt', 'w')
texto = """ Lista de alunos: João da Silva, José Lima, Maria das Dores. """
arq.write(texto)
arq.close()
print(texto)
