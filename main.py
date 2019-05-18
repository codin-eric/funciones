'''
Coding-eric video 12
Funciones
'''

def my_func(nombre):
	print(f"soy {nombre}")


# my_func("Eric")

def suma(a,b):
	res = a + b
	return "soy una suma", res


tipo, resultado = suma(3,4)

# print(tipo)
# print(resultado)

import random

def get_stats():
	dados = [random.randint(1,6) for i in range(4)]
	dados.sort()
	max_dados = dados[1:]
	return sum(max_dados)

stats = {
	"str": get_stats(),
	"des": get_stats(),
	"int": get_stats(),
	"wis": get_stats(),
	"con": get_stats(),
}

print(stats)