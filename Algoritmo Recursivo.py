def fatorial(n):
  # Caso base: fatorial de 0 é 1
  if n == 0:
    return 1
  # Caso recursivo: n! = n * (n-1)!
  else:
    return n * fatorial(n-1)
