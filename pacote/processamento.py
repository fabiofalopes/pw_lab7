def positivo(n):
    return (n > 0)

def par(n):
    return(n%2 == 0)

def primo(n,i):
    # Metodo recursivo, chamado com i = 2
    # Corner cases
    if (n == 0 or n == 1):
        return False

    # Checking Prime
    if (n == i):
        return True
 
    # Base cases
    if (n % i == 0):
        return False
 
    i += 1
 
    return primo(n, i)