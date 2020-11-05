from prettytable import PrettyTable 
import pymysql

connection = pymysql.connect(
    host = "localhost",
    user = "root",
#    passwd = "TuContraseña",
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
        table.field_names = ["idUsuarios", "nombre", "apellido", "segundoApellido", "telefono", "idioma", "correoElectronico", "contrasenna", "direccion"]
        for cliente in result:
            table.add_row([cliente["idUsuarios"], cliente["nombre"], cliente["apellido"], cliente["segundoApellido"], cliente["telefono"], cliente["idioma"], cliente["correoElectronico"], cliente["contrasenna"], cliente["direccion"]])
        print(table)
        

def addUsuario():
    print("Añadirás un nuevo cliente")
    name = input("Nombre: ")
    apellido = input("Apellido: ")
    segundoApellido = input("Segundo apellido: ")
    telefono = input("Número de teléfono: ")
    idioma = input("Idioma: ")
    correoElectronico = input("Correo electrónico: ")
    contrasenna = input("Contraseña: ")
    direccion = input("Dirección: ")

    try:
        with connection.cursor() as cursor:
            sql = f"insert into ikea.usuarios (nombre, apellido, segundoApellido, telefono, idioma, correoElectronico, contrasenna, direccion) values ('{name}','{apellido}','{segundoApellido}','{telefono}','{idioma}','{correoElectronico}','{contrasenna}','{direccion}');"
            cursor.execute(sql)
            connection.commit()

    finally:
        getAllUsuarios()



def deleteUsuario():
    result = []
    print("Borrarás un registro de la tabla usuarios")
    getAllUsuarios()
    idDel = int(input("Id del usuario a borrar: "))

    try:
        with connection.cursor() as cursor:
            sql = f"select idUsuarios, nombre, apellido, segundoApellido from ikea.usuarios where idUsuarios = {idDel}; "
            indicacion = f"delete from ikea.usuarios where idUsuarios = {idDel};"
            cursor.execute(sql)
            result = cursor.fetchall()
            registro = (result[0])
            datosReg = str(registro['idUsuarios']) + " " + registro['nombre'] + " " + registro['apellido'] + " " + registro['segundoApellido']
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
            nombre = registro['nombre']
            apellido = registro['apellido']
            segundoApellido = registro['segundoApellido']
            telefono = registro['telefono']
            idioma = registro['idioma']
            correo = registro['correoElectronico']
            contra = registro['contrasenna']
            direccion = registro['direccion'] 
            datosReg = str(registro['idUsuarios']) + " " + nombre + " " + apellido + " " + segundoApellido + " " + telefono + " " + idioma + " " + correo+ " " + contra + " " + direccion
            print(datosReg)

            option = int(input("Actualizar nombre? 1-Si, 0-No"))
            if option == 1:
                print("Nombre actual: " + nombre)
                NuevoNombre = input("Nuevo nombre: ")
                nombre = NuevoNombre

            else:
                nombre = nombre

            option = int(input("Actualizar apellido? 1-Si, 0-No"))
            if option == 1:
                print("Apellido actual: " + apellido)
                NuevoApellido = input("Nuevo apellido: ")
                apellido = NuevoApellido

            else:
                apellido = apellido


            option = int(input("Actualizar segundo apellido? 1-Si, 0-No"))
            if option == 1:
                print("Segundo apellido actual: " + segundoApellido)
                NuevoSegundoApellido = input("Nuevo segundo apellido: ")
                segundoApellido = NuevoSegundoApellido

            else:
                segundoApellido = segundoApellido

            
            option = int(input("Actualizar teléfono? 1-Si, 0-No"))
            if option == 1:
                print("Telefono actual: " + telefono)
                NuevoTelefono = input("Nuevo telefono: ")
                telefono = NuevoTelefono

            else:
                telefono = telefono


            option = int(input("Actualizar idioma? 1-Si, 0-No"))
            if option == 1:
                print("Idioma actual: " + idioma)
                NuevoIdioma = input("Nuevo idioma: ")
                idioma = NuevoIdioma

            else:
                idioma = idioma


            option = int(input("Actualizar correo electrónico? 1-Si, 0-No"))
            if option == 1:
                print("Correo electrónico actual: " + correo)
                NuevoCorreo = input("Nuevo correo: ")
                correo = NuevoCorreo

            else:
                correo = correo

            
            option = int(input("Actualizar contraseña? 1-Si, 0-No"))
            if option == 1:
                print("Contraseña actual: " + contra)
                NuevaContra = input("Nueva contraseña: ")
                contra = NuevaContra

            else:
                contra = contra


            option = int(input("Actualizar dirección? 1-Si, 0-No"))
            if option == 1:
                print("Dirección actual: " + direccion)
                NuevaDireccion = input("Nueva dirección: ")
                direccion = NuevaDireccion

            else:
                direccion = direccion


            indicacion = f"UPDATE ikea.usuarios SET idUsuarios = '{user}', nombre = '{nombre}', apellido = '{apellido}', segundoApellido = '{segundoApellido}', telefono = '{telefono}', idioma = '{idioma}', correoElectronico = '{correo}', contrasenna = '{contra}', direccion = '{direccion}' where idUsuarios = '{user}';"
            cursor.execute(indicacion)
            connection.commit()
            getAllUsuarios()


    finally:
        pass

