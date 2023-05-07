productos = {
    "1": ["Manzanas" , 5000.0 , 25], 
    "2": ["Limones" , 2300.0 , 15], 
    "3": ["Peras" , 2700.0 , 33], 
    "4": ["Arandanos" , 9300.0 , 5 ], 
    "5": ["Tomates" , 2100.0 , 42], 
    "6": ["Fresas" , 4100.0 , 3 ], 
    "7": ["Helado" , 4500.0 , 41], 
    "8": ["Galletas" , 500.0 , 8 ], 
    "9": ["Chocolates", 3500.0 , 80], 
    "10": ["Jamon" , 15000.0 , 10] 
}
def agregar(codigo, lista):
  if productos.get(codigo) == None:
    productos[codigo] = lista
    return 1
  return -1

def actualizar(codigo, lista):
  if productos.get(codigo) != None:
    productos[codigo] = lista
    return 1
  return -1

def eliminar(codigo):
  if productos.get(codigo) != None:
    productos.pop(codigo)
    return 1
  return -1

def mayor(productos):
  mayor =0
  nombre = ""
  for _, valor in productos.items():
    if valor[1] > mayor:
      mayor = valor[1]
      nombre = valor[0]
  return nombre

def menor(productos):
  menor = 1000000
  nombre = ""
  for _, valor in productos.items():
    if valor[1]< menor:
      menor = valor[1]
      nombre = valor[0]
  return nombre

def promedio(productos):
  suma = 0
  for _, valor in productos.items():
    suma+=valor[1]
  return suma/len(productos)

def total_inventario(productos):
  inventario = 0
  for _, valor in productos.items():
    inventario+=(valor[1]*valor[2])
  return inventario

operacion = input()
codigo, *producto = input().split()
salida = 0
if operacion == 'AGREGAR':
  producto[1] = float(producto[1])
  producto[2] = int(producto[2])
  salida = agregar(codigo, producto)
elif operacion == 'ACTUALIZAR':
  producto[1] = float(producto[1])
  producto[2] = int(producto[2])
  salida = actualizar(codigo, producto)
elif operacion == "BORRAR":
  producto[1] = float(producto[1])
  producto[2] = int(producto[2])
  salida = eliminar(codigo)
if salida == 1:
  print(f'{mayor(productos)} {menor(productos)} {round(promedio(productos),1)} {round(total_inventario(productos),1)}')
else:
  print('ERROR')
