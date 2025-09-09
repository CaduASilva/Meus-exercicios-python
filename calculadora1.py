   #funções

def somar(a, b):
    resultado = a + b
    return resultado

def subtrair(a, b):
    resultado = a - b
    return resultado

def multiplicar(a, b):
    resultado = a * b
    return resultado

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por 0"
    return a / b

def pedir_num(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except:
          print("Erro! Por favor, digite apenas números.")


    #início da calculadora

a = pedir_num("Digite um número: " )
b = pedir_num("Digite outro numero: ")

while True:

    operador = input("escolha um operador: +|-|*|/ : ")

    if operador == "+":
         resultado = somar(a, b)
         print(f"A soma é: {resultado}")
         break
         
    elif operador == "-":
         resultado = subtrair(a, b)
         print(f"A subtração é: {resultado}")
         break
    elif operador == "*":
         resultado = multiplicar(a, b)
         print(f"A multiplicação é: {resultado}")
         break
    elif operador == "/":
         resultado = dividir(a, b)
         print(f"A divisão é: {resultado}")
         break
    else:
         print("Você não digitou um operador")