# Juan David Saenz Reyes
# 213022A_2201
# Ingenieria de sistemas
# Fundamentos de programacion 
# Codigo fuente: Autoria propia

# Matriz del inventario
inventario = [
    ["A101", "Teclado", 3, 10],
    ["A102", "Mouse", 12, 10],
    ["A103", "Monitor", 2, 5],
    ["A104", "USB", 20, 15],
    ["A105", "Impresora", 1, 4]
]
# Función para calcular la cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0

    return cantidad

# Mostrar lista de pedidos
print("LISTA DE PEDIDOS")
print("---------------------------")

for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    print("Artículo:", nombre)
    print("Cantidad a pedir:", cantidad_pedir)
    print("---------------------------")
    
