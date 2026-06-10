def es_primo_miller_rabin(numero, k=5):

    """
    Comprueba si un número es primo usando test probabilístico (Miller-Rabin).
    
    Parámetros:
        n (int): número a evaluar
    
    Devuelve:
        bool: True si probablemente primo, False si compuesto
    """

    import random

    # Casos pequeños: ni 0, ni 1, ni pares mayores son primos.
    if numero < 2:
        return False
    if numero == 2 or numero == 3:
        return True
    if numero % 2 == 0:
        return False

    # Descomponer numero - 1 como 2^r * d con d impar.
    # Ejemplo: para n=41, n-1=40=2^3*5, r=3, d=5.
    r, d = 0, numero - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Cada ronda usa una base distinta y verifica si n se comporta como primo.
    for _ in range(k):
        a = random.randrange(2, numero - 1)

        # x = a^d mod numero. Si x es 1 o n-1, la ronda pasa inmediatamente.
        x = pow(a, d, numero)
        if x == 1 or x == numero - 1:
            continue

        # Si x no es 1 ni n-1, comprobamos la secuencia de cuadrados:
        # x, x^2, x^4, x^8, ... modulo n.
        # Para un primo, esta secuencia debe llegar a n-1 antes de terminar.
        for _ in range(r - 1):
            x = pow(x, 2, numero)
            if x == numero - 1:
                break
        else:
            # Si nunca aparece n-1, la base a demuestra que n es compuesto.
            return False

    # Si ninguna base descartó a n, entonces n es probablemente primo.
    return True

# Ejemplo de uso:
print(es_primo_miller_rabin(61, 5))
print(es_primo_miller_rabin(24815323469403931728221172233738523533528335161133543380459461440894543366372904768334987263999999999999999999663, 1))
