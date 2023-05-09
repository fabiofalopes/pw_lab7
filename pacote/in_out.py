def ler_numero():
    while True:
        try:
            value = int(input("Introduza um numero "))
            return value
        except ValueError:
            print("Input invalido. Valor tem que ser numerico.") 
    
    
def imprime_resultados(n, positivo, par):
    #imprime_resultados(n, positivo, par), que imprime uma frase usando os argumentos (n: numero inserido, positivo: variável booleana que 
    #indica se é positivo, par: variável booleana que indica se é par)
    if positivo:
        sinal = "é positivo"
    else:
        sinal = "não é positivo"
    if par:
        paridade = "é par"
    else:
        paridade = "é impar"
    print(f"n: O numero {n}, {sinal} e {paridade}")

    
def menu():
    print("1. Check if a number is positive")
    print("2. Check if a number is even")
    print("3. Check if a number is prime")
    print("4. Exit")