#Complete as funcoes a seguir

def soma(a, b):
	print("A soma deu", a + b)

def subtrai(a, b):
	print("A subtração deu", a - b)

def multiplica(a, b):
	print("A multiplicação deu", a * b)

def divide(a, b):
	if(b == 0):
		print("Não é possivel dividir por 0")
	else:
		print("A divisão deu", a / b)


print("Calculadora simples")

num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))

soma(num1, num2)
subtrai(num1, num2)
multiplica(num1, num2)
divide(num1, num2)