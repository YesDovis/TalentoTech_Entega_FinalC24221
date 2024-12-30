index_global = 3

lista_de_productos = {
    1:{"nombre":"Barba Roja","precio":3000, "stock":10, "categoria":"artesanal"},
    2:{"nombre":"Sir lupulo","precio":4000, "stock":20, "categoria":"artesanal"},
    3:{"nombre":"Strange","precio":5000, "stock":10, "categoria":"artesanal" }
    }


def registrar_producto(datos_producto):
    global index_global
    index_global += 1
    lista_de_productos[index_global] = datos_producto

    

def mostrar_productos():
    print("<----- Lista de Productos ------>")
    print(f"INDEX      |       Datos")
    for key in lista_de_productos:        
        print(f"{key}: {lista_de_productos[key]}")
    input("Presione Enter para continuar...")


def actualizar_producto(key_producto):
    if key_producto in lista_de_productos:
        print(f"Seleccionaste el producto: {lista_de_productos[key_producto]}")
        nombre = input("Ingrese el nuevo nombre: ")
        precio = input("Ingrese el nuevo precio: ")
        stock = input("Ingrese el nuevo stock: ")
        categoria = input("Ingrese la nueva categoría: ")

        if precio.isdigit() and stock.isdigit():
            lista_de_productos[key_producto] = {
                "nombre": nombre,
                "precio": int(precio),
                "stock": int(stock),
                "categoria": categoria,
            }
            print("Producto actualizado con éxito.")
        else:
            print("Precio y stock deben ser valores numéricos.")
    else:
        print("Producto no encontrado")





def buscar_producto(index):
    if index in lista_de_productos:
        print(f'''
                Datos del producto:
                
                Nombre:{lista_de_productos[index]["nombre"]}
                Precio:{lista_de_productos[index]["precio"]}
                Stock:{lista_de_productos[index]["stock"]}
                Categoria:{lista_de_productos[index]["categoria"]}
                ''')
        input()
    else:
        print("Producto no encontrado")
    input("Presione Enter para continuar...")



def eliminar_producto(index):
    if index in lista_de_productos:
        eliminado = lista_de_productos.pop(index)
        print(f"Producto eliminado: {eliminado}")
    else:
        print("Producto eliminado")
    input("Presione Enter para continuar...")



def reporte_bajo_stock(limite):
    print(f"Productos con stock menor o igual a {limite}:")
    encontrados = [
        producto
        for producto in lista_de_productos.values()
        if producto["stock"] <= limite
    ]
    if encontrados:
        for producto in encontrados:
            print(producto)
    else:
        print("No se encontraron productos con bajo stock.")
    input("Presione Enter para continuar...")



#reporte_bajo_stock(30)
#actualizar_producto(1)




#buscar_producto(1)
#eliminar_producto(1)
#mostrar_productos()



# Menú principal

opcion = ""

while opcion != "7":
    print("-" * 70) 
    print("Bienvenidos a 'La Birra es Bella'\n")
    print("-" * 70) 
    opcion = input(f'''Ingrese la opcion: 
                            1) Agregar producto 
                            2) Mostrar lista de productos 
                            3) Eliminar Producto 
                            4) Actualizar un Producto
                            5) Buscas un producto por id
                            6) Alerta Stock
                            7) Salir
                            Ingrese su opcion: ''')
    print("-" * 70) 
    

# Opción 1: Agregar un nuevo Producto
    if opcion == "1":
        nombre = input("Ingrese el  nombre: ")
        precio = int(input("Ingrese el precio: "))        
        stock = int(input("Ingrese el stock: "))
        categoria = input("Ingrese la categoria: ")
        if precio > 0 and stock > 0:
            datos_producto = {"nombre":nombre,"precio":precio,"stock":stock,"categoria":categoria}
            registrar_producto(datos_producto)
            index_global = index_global + 1
        else:
            print("Datos incorrectos")

# Opción 2: Mostrar 

    elif opcion == "2":
        mostrar_productos()

# Opción 3: Eiminar
    elif opcion == "3":
        mostrar_productos()
        ingreso_usuario = int(input("Ingrese el id del producto que desea eliminar"))
        eliminar_producto(ingreso_usuario)

# Opción 4: actualizar

    elif opcion == "4":
        mostrar_productos()
        ingreso_usuario = int(input("Ingrese el id del producto que desea actualizar"))
        actualizar_producto(ingreso_usuario)

# Opción 5: Buscar

    elif opcion == "5":
        ingreso_usuario = int(input("Ingrese el id del producto que desea buscar"))
        buscar_producto(ingreso_usuario)

# Opción 6:  Connsulta

    elif opcion == "6":
        ingreso_usuario = int(input("Ingrese el limite de stock a consultar"))
        reporte_bajo_stock(ingreso_usuario)

# Opción 7: Salida

    elif opcion == 7:
        print("Vuelva prontossss.")
    else:
        print("Opción no encontrada. Intente de nuevo.")