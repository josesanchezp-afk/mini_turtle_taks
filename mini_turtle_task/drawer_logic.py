derechar = 5
izquierda = 5
escalones = 0

def derecha(n):
  global escalones
  espaciosIzquierda = " " * derechar * escalones
  print(espaciosIzquierda + "-" * n + ">")

def abajo(n):
  global escalones
  espaciosIzquierda = " " * derechar * escalones
  print((espaciosIzquierda + (" " * derechar + "|\n")) * n + (espaciosIzquierda + " " * derechar + "V"))
  escalones = escalones + 1

def reiniciar():
  global escalones
  escalones = 0