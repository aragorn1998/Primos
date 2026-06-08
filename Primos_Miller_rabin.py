def es_primo_miller_rabin(numero, k=5):
    """
    Test probabilístico de primalidad de Miller-Rabin.

    El objetivo es distinguir entre:
      - compuesto: se detecta con seguridad,
      - probablemente primo: no se detecta compuesto tras k pruebas.

    Pasos del algoritmo:
      1. Rechazar los casos triviales: menores de 2, pares y 2 o 3.
      2. Escribir n-1 como 2^r * d con d impar.
         Esta descomposición es clave, porque el test explora
         la secuencia de potencias de a sobre n.
      3. Repetir k rondas independientes:
         a. Elegir una base aleatoria a en [2, n-2].
         b. Calcular x = a^d mod n.
         c. Si x es 1 o n-1, entonces n pasa la ronda.
         d. Si no, elevar x al cuadrado hasta r-1 veces.
            Si en alguna iteración x se convierte en n-1,
            entonces n también pasa la ronda.
         e. Si nunca aparece n-1, n es compuesto.
      4. Si n pasa todas las rondas, es "probablemente primo".

    Explicación matemática resumida:
      - Para un número primo p, los únicos cuadrados con valor 1 modulo p
        son 1 y p-1. Por eso si x = a^d mod p no es 1 ni p-1,
        iterar x = x^2 mod p debe terminar en p-1 si p es primo.
      - Si n es compuesto, hay pocas bases a que imitan este comportamiento.
        Cada ronda reduce mucho la probabilidad de error.

    Args:
        numero: Entero positivo a verificar.
        k: Número de rondas independientes del test.
           Más rondas reducen la probabilidad de clasificar un compuesto como primo.

    Returns:
        True si numero es probablemente primo.
        False si numero es definitivamente compuesto.
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
        print(a, x)
        if x == 1 or x == numero - 1:
            continue

        # Si x no es 1 ni n-1, comprobamos la secuencia de cuadrados:
        # x, x^2, x^4, x^8, ... modulo n.
        # Para un primo, esta secuencia debe llegar a n-1 antes de terminar.
        for _ in range(r - 1):
            x = pow(x, 2, numero)
            print(x)
            if x == numero - 1:
                break
        else:
            # Si nunca aparece n-1, la base a demuestra que n es compuesto.
            return False

    # Si ninguna base descartó a n, entonces n es probablemente primo.
    return True

# Ejemplo de uso:
print(es_primo_miller_rabin(61, 5))
