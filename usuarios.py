from prettytable import PrettyTable 
import pymysql

connection = pymysql.connect(
    host = "localhost",
    user = "root",
#    passwd = "12345",
    db= "ikea",
    cursorclass = pymysql.cursors.DictCursor,
)



def getAllUsuarios():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM ikea.usuarios;"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        table = PrettyTable()
        table.field_names = ["idUsuarios", "nombreUsuario" ,"nombre", "apellido", "segundoApellido", "telefono", "idioma", "correoElectronico", "contrasenna", "direccion"]
        for cliente in result:
            table.add_row([cliente["idUsuarios"], cliente["nombreUsuario"] ,cliente["nombre"], cliente["apellido"], cliente["segundoApellido"], cliente["telefono"], cliente["idioma"], cliente["correoElectronico"], cliente["contrasenna"], cliente["direccion"]])
        print(table)
        

def addUsuario():
    print("Crearás un nuevo Usuario")
    name = input("Nombre: ")
    apellido = input("Apellido: ")
    segundoApellido = input("Segundo apellido: ")
    username = input("Usuario: ")
    telefono = input("Número de teléfono: ")
    idioma = input("Idioma: ")
    correoElectronico = input("Correo electrónico: ")
    contrasenna = input("Contraseña: ")
    contrasenna2 = input("Confirma tu contraseña: ")
    direccion = input("Dirección: ")
    Existe = False
    users = []
    usuarios = []

    if contrasenna == contrasenna2:
        try:
            with connection.cursor() as cursor:
                sql = f"select nombreUsuario from ikea.Usuarios;"
                cursor.execute(sql)
                users = cursor.fetchall()
                for user in users:
                    usuarios.append(user['nombreUsuario'])    

                Existe = username in usuarios

                if Existe == True:
                    print(" ")
                    print("---------------------------------------------------")
                    print(" ")
                    print("Este nombre de usuario ya está registrado, vuelve a intentarlo")
                    print(" ")
                    print("---------------------------------------------------")
                    print(" ")
                    addUsuario()

                else:
                    print(" ")
                    print("---------------------------------------------------")
                    print(" ")
                    BuscarProducto()
                    sql = f"insert into ikea.usuarios (nombreUsuario, nombre, apellido, segundoApellido, telefono, idioma, correoElectronico, contrasenna, direccion) values ('{username}','{name}','{apellido}','{segundoApellido}','{telefono}','{idioma}','{correoElectronico}','{contrasenna}', '{direccion}');"
                    cursor.execute(sql)
                    connection.commit()
                    print(" ")
                    print("---------------------------------------------------")
                    print(" ")

        finally:
            pass

    else:
        print(" ")
        print("---------------------------------------------------")
        print(" ")
        print("Las contraseñas ingresadas no corresponden, vuelve a intentarlo")
        print(" ")
        print("---------------------------------------------------")
        print(" ")
        addUsuario()



def deleteUsuario():
    result = []
    print("Borrarás un registro de la tabla usuarios")
    getAllUsuarios()
    idDel = int(input("Id del usuario a borrar: "))

    try:
        with connection.cursor() as cursor:
            sql = f"select idUsuarios, nombreUsuario, nombre, apellido, segundoApellido from ikea.usuarios where idUsuarios = {idDel}; "
            indicacion = f"delete from ikea.usuarios where idUsuarios = {idDel};"
            cursor.execute(sql)
            result = cursor.fetchall()
            registro = (result[0])
            datosReg = str(registro['idUsuarios']) + " " + registro['nombreUsuario'] + " " + registro['nombre'] + " " + registro['apellido'] + " " + registro['segundoApellido']
            print("Usuario: " + datosReg)
            print("Borrarás definitivamente el registro anterior. Estás seguro?")
            opcion = int(input("Si(1), No(0). Escribe 1 o 0."))

            if opcion == 1:
                cursor.execute(indicacion)
                connection.commit()
                print("Se ha borrado definitivamente el registro: " + datosReg)
                getAllUsuarios()

            else:
                print("No se ha eliminado ningún registro de la tabla Usuarios")
                getAllUsuarios()


    finally:
        pass


def updateUsuario():
    print("Modificarás un registro de la tabla Usuarios")
    getAllUsuarios()
    IdUpdate = int(input("Id del usuario a modificar: "))
    result = []

    try:
        with connection.cursor() as cursor:
            sql = f"select * from ikea.usuarios where idUsuarios = '{IdUpdate}'; "
            cursor.execute(sql)
            result = cursor.fetchall()
            registro = (result[0])
            user = str(registro['idUsuarios'])
            username = str(registro['nombreUsuario'])
            nombre = registro['nombre']
            apellido = registro['apellido']
            segundoApellido = registro['segundoApellido']
            telefono = registro['telefono']
            idioma = registro['idioma']
            correo = registro['correoElectronico']
            contra = registro['contrasenna']
            direccion = registro['direccion']

            datosReg = str(registro['idUsuarios']) + " " + username + " " + nombre + " " + apellido + " " + segundoApellido + " " + telefono + " " + idioma + " " + correo+ " " + contra + " " + direccion
            print(datosReg)


            option = int(input("Actualizar nombre? 1-Si, 0-No: "))
            if option == 1:
                print("Nombre actual: " + nombre)
                NuevoNombre = input("Nuevo nombre: ")
                nombre = NuevoNombre

            else:
                nombre = nombre

            option = int(input("Actualizar apellido? 1-Si, 0-No: "))
            if option == 1:
                print("Apellido actual: " + apellido)
                NuevoApellido = input("Nuevo apellido: ")
                apellido = NuevoApellido

            else:
                apellido = apellido


            option = int(input("Actualizar segundo apellido? 1-Si, 0-No: "))
            if option == 1:
                print("Segundo apellido actual: " + segundoApellido)
                NuevoSegundoApellido = input("Nuevo segundo apellido: ")
                segundoApellido = NuevoSegundoApellido

            else:
                segundoApellido = segundoApellido

            
            option = int(input("Actualizar teléfono? 1-Si, 0-No: "))
            if option == 1:
                print("Telefono actual: " + telefono)
                NuevoTelefono = input("Nuevo telefono: ")
                telefono = NuevoTelefono

            else:
                telefono = telefono


            option = int(input("Actualizar idioma? 1-Si, 0-No: "))
            if option == 1:
                print("Idioma actual: " + idioma)
                NuevoIdioma = input("Nuevo idioma: ")
                idioma = NuevoIdioma

            else:
                idioma = idioma


            option = int(input("Actualizar correo electrónico? 1-Si, 0-No: "))
            if option == 1:
                print("Correo electrónico actual: " + correo)
                NuevoCorreo = input("Nuevo correo: ")
                correo = NuevoCorreo

            else:
                correo = correo

            
            option = int(input("Actualizar contraseña? 1-Si, 0-No: "))
            if option == 1:
                print("Contraseña actual: " + contra)
                NuevaContra = input("Nueva contraseña: ")
                contra = NuevaContra

            else:
                contra = contra


            option = int(input("Actualizar dirección? 1-Si, 0-No: "))
            if option == 1:
                print("Dirección actual: " + direccion)
                NuevaDireccion = input("Nueva dirección: ")
                direccion = NuevaDireccion

            else:
                direccion = direccion


            indicacion = f"UPDATE ikea.usuarios SET idUsuarios = {user}, nombreUsuario = '{username}', nombre = '{nombre}', apellido = '{apellido}', segundoApellido = '{segundoApellido}', telefono = '{telefono}', idioma = '{idioma}', correoElectronico = '{correo}', contrasenna = '{contra}', direccion = '{direccion}' where idUsuarios = '{user}';"
            cursor.execute(indicacion)
            connection.commit()
            getAllUsuarios()


    finally:
        pass


def login():
    Username = str(input("Nombre Usuario: "))
    Contrasenna = str(input("Contraseña: "))
    Existe = False
    users = []
    username = []
    try:
        with connection.cursor() as cursor:
            sql = f"select nombreUsuario from ikea.Usuarios;"
            cursor.execute(sql)
            users = cursor.fetchall()
            for user in users:
                username.append(user['nombreUsuario'])    

            Existe = Username in username

            if Existe == True:
                sql2 = f"select contrasenna from ikea.usuarios where nombreUsuario = '{Username}';"
                cursor.execute(sql2)
                resulta = cursor.fetchall()
                psw2 = resulta[0]
                password = psw2['contrasenna']
                
                if Contrasenna == password:
                    print(" ")
                    BuscarProducto()

                else:
                    print("El usuario o la contraseña están incorrectas, vuelve a intentarlo")
                    login()

            
            else:
                print("No se ha encontrado este nombre de usuario, vuelve a intentarlo")
                login()

    finally:
        pass

def Operar():
    print("Bienvenido a IKEA")
    print("De qué manera deseas operar la aplicación?")
    print("1. Usuario")
    print("2. Administrador")

    opcion = int(input("Opción: "))

    if opcion == 1:
        print("----------------------")
        print("Usarás la app cómo usuario")
        print("1. Iniciar sesión con cuenta ya existente")
        print("2. Crear una nueva cuenta")
        print(" ")

        option = int(input("Opción: "))

        if option == 1:
            print("----------------------")
            login()

        else:
            print("----------------------")
            addUsuario()
          

def BuscarProducto():
    while True:
        print(" ")
        print("Has iniciado sesión exitosamente")
        print(" ")
        print("Cómo deseas realizar tu búsqueda?")
        print("1. Escribir lo que buscas")
        print("2. Directorio de categorías")
        print(" ")
        opcion = int(input("Opción: "))

        if opcion == 1:
            producto = input("Qué buscas? ")
            try:
                with connection.cursor() as cursor:
                    sql = f"select ikea.categoriasproductos.nombre, ikea.claseproductos.nombre, ikea.productos.idProductos, ikea.productos.nombre, ikea.productos.precio, ikea.productos.dimensiones, ikea.productos.materiales, ikea.productos.coloresDisponibles, ikea.productos.descripcion, ikea.productos.garantia from ikea.categoriasproductos inner join ikea.claseproductos on ikea.claseproductos.idCategoriasProductos = ikea.categoriasproductos.idCategoriasProductos inner join ikea.productos on ikea.productos.idClaseProductos = ikea.claseproductos.idClaseProductos where ikea.categoriasproductos.nombre = '{producto}' or ikea.claseproductos.nombre = '{producto}' or ikea.productos.nombre = '{producto}';"
                    cursor.execute(sql)
                    result = cursor.fetchall()
            
            finally:
                table = PrettyTable()
                table.field_names = ["Categoría", "Clase" ,"idProducto", "Nombre producto", "Precio", "Dimensiones", "Materiales", "Colores disponibles", "Descripción", "Garantía"]
                for product in result:
                    table.add_row([product["nombre"], product["claseproductos.nombre"] ,product["idProductos"], product["productos.nombre"], product["precio"], product["dimensiones"], product["materiales"], product["coloresDisponibles"], product["descripcion"], product["garantia"]])
                print(" ")
                print(" ")
                print("Estos son todos los productos que se han encontrado con tu busqueda: " + str(producto))
                print(table)
                print(" ")
                dec = int(input("Deseas seguir buscando productos? 1: Si, 0: No "))
                if dec == 1:
                    BuscarProducto()
                else:
                     break

        else:
            print("Estas son las categorías de productos")
            listaCategorias = []
            listaClases = []
            intA = 1
            intC = 1
            try:
                with connection.cursor() as cursor:
                    sql = f"select ikea.categoriasproductos.nombre from ikea.categoriasproductos;"
                    Dict = {}
                    Dict2 = {}
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    for category in result:
                        listaCategorias.append(category['nombre'])

                    for cat in listaCategorias:
                        print(str(intC) + "." + cat)
                        Dict.update({intC:cat})
                        intC = intC + 1
                    

                    option = int(input("Qué categoría de producto deseas buscar?"))
                    categoria = Dict[option]
                    
                    sql2 = f"select ikea.claseproductos.nombre from ikea.claseproductos inner join ikea.categoriasproductos on ikea.claseproductos.idCategoriasProductos = ikea.categoriasproductos.idCategoriasProductos where ikea.categoriasproductos.nombre = '{categoria}'"
                    cursor.execute(sql2)
                    result2 = cursor.fetchall()


                    for clase in result2:
                        listaClases.append(clase['nombre'])

                    for cla in listaClases:
                        print(str(intA) + "." + cla)
                        Dict2.update({intA:cla})
                        intA = intA + 1

                    num = int(input("Qué clase de producto de deseas buscar?"))
                    clath = Dict2[num]

                    sql3 = f"select ikea.productos.idProductos, ikea.productos.nombre, ikea.productos.precio, ikea.productos.dimensiones, ikea.productos.materiales, ikea.productos.coloresDisponibles, ikea.productos.descripcion, ikea.productos.garantia from ikea.productos inner join ikea.claseproductos on ikea.productos.idClaseProductos = ikea.claseproductos.idClaseProductos where ikea.claseproductos.nombre = '{clath}';"
                    cursor.execute(sql3)
                    result3 = cursor.fetchall()

            finally: 
                table2 = PrettyTable()
                table2.field_names = ["idProdcto", "Nombre Producto" ,"Precio", "Dimensiones", "Materiales", "Colores Disponibles", "Descripción", "Garantía"]
                for product in result3:
                    table2.add_row([product["idProductos"], product["nombre"] ,product["precio"], product["dimensiones"], product["materiales"], product["coloresDisponibles"], product["descripcion"], product["garantia"]])
                print(" ")
                print("Estos son los resultados de tu búsqueda ")
                print(table2)

                dec = int(input("Deseas seguir buscando productos? 1: Si, 0: No "))
                if dec == 1:
                    BuscarProducto()
                else:
                     break        
