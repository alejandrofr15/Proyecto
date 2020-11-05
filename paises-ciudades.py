from prettytable import PrettyTable 
import pymysql

#Conexión a Servidor
connection = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd = "12345",
    db= "ikea",
    cursorclass = pymysql.cursors.DictCursor,
)

#Tabla Países
        #Obtener todos los registros de una tabla
def getAllPaises():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM ikea.paises;"
            cursor.execute(sql)
            result = cursor.fetchall()

    finally:
        table = PrettyTable()
        table.field_names = ["idPaises", "nombre"]
        for pais in result:
            table.add_row([pais["idPaises"], pais["nombre"]])
        print(table)


        #Agregar un nuevo registro a una tabla
def addNewPais():
    print("Añadirás un nuevo país a la tabla Paises")
    nombre = input("Nombre País: ")


    try:
        with connection.cursor() as cursor:
            sql = f"insert into ikea.paises (nombre) values ('{nombre}');"
            cursor.execute(sql)
            connection.commit()

    finally:
        getAllPaises()


        #Borrar un registro
def deletePais():
    result = []
    print("Borrarás un registro de la tabla Países")
    getAllPaises()
    idDel = int(input("Id del país a borrar: "))

    try:
        with connection.cursor() as cursor:
            sql = f"select * from ikea.paises where idPaises = {idDel}; " 
            indicacion = f"delete from ikea.paises where idPaises = {idDel}; "
            cursor.execute(sql)
            result = cursor.fetchall()
            registro = (result[0])
            datosReg = str(registro['idPaises']) + " " + registro['nombre'] 
            print(datosReg)
            print("Borrarás definitivamente el registro anterior. Estás seguro?")
            opcion = int(input("Si(1), No(0). Escribe 1 o 0."))

            if opcion == 1:
                cursor.execute(indicacion)
                connection.commit()
                print("Se ha borrado definitivamente el registro de la tabla Países: " + datosReg)
                getAllPaises()

            else:
                print("No se ha eliminado ningún registro de la tabla Países")
                getAllPaises()


    finally:
        pass


        #Actualizar un registro
def updatePais():
    print("Modificarás un registro de la tabla Países")
    getAllPaises()
    IdUpdate = int(input("Id del país a modificar: "))
    result = []

    try:
        with connection.cursor() as cursor:
            sql = f"select * from ikea.paises where idPaises = '{IdUpdate}'; "
            cursor.execute(sql)
            result = cursor.fetchall()
            registro = (result[0])
            user = str(registro['idPaises'])
            nombre = registro['nombre']
             
            datosReg = user + " " + nombre 
            print(datosReg)

            option = int(input("Actualizar nombre? 1-Si, 0-No"))
            if option == 1:
                print("Nombre actual: " + nombre)
                NuevoNombre = input("Nuevo nombre: ")
                nombre = NuevoNombre

            else:
                nombre = nombre


            indicacion = f"UPDATE ikea.paises SET idPaises = '{user}', nombre = '{nombre}' where idPaises = '{user}';"
            cursor.execute(indicacion)
            connection.commit()
            getAllPaises()


    finally:
        pass


#Tabla Ciudades

        #Obtener todas las ciudades
def getAllCiudades():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM ikea.ciudades;"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        table = PrettyTable()
        table.field_names = ["idCiudades", "nombre", "idPaises"]
        for ciudad in result:
            table.add_row([ciudad["idCiudades"], ciudad["nombre"], ciudad["idPaises"]])
        print(table)

        #Ingresar una nueva ciudad
def addNewCiudad():
    print("Añadirás una nueva ciudad a la tabla Ciudades")
    nombre = input("Nombre Ciudad: ")
    getAllPaises()
    pais = str(input("Id del país: "))


    try:
        with connection.cursor() as cursor:
            sql = f"insert into ikea.ciudades (nombre, idPaises) values ('{nombre}', '{pais}');"
            cursor.execute(sql)
            connection.commit()

    finally:
        getAllCiudades()


        #Borrar una ciudad 
def deleteCiudad():
    result = []
    print("Borrarás un registro de la tabla Ciudades")
    getAllCiudades()
    idDel = int(input("Id de la ciudad a borrar: "))

    try:
        with connection.cursor() as cursor:
            sql = f"select * from ikea.ciudades where idCiudades = {idDel}; "
            indicacion = f"delete from ikea.ciudades where idCiudades = {idDel};"
            cursor.execute(sql)
            result = cursor.fetchall()
            registro = (result[0])
            datosReg = str(registro['idCiudades']) + " " + registro['nombre'] + " " + str(registro['idPaises']) 
            print("idCiudad: " + str(registro['idCiudades']) + " Nombre: " + registro['nombre'] + " País: " + str(registro['idPaises']))
            print("Borrarás definitivamente el registro anterior. Estás seguro?")
            opcion = int(input("Si(1), No(0). Escribe 1 o 0."))

            if opcion == 1:
                cursor.execute(indicacion)
                connection.commit()
                print("Se ha borrado definitivamente el registro: " + datosReg)
                getAllCiudades()

            else:
                print("No se ha eliminado ningún registro de la tabla Ciudades")
                getAllCiudades()


    finally:
        pass

        #Actualizar una ciudad
def updateCiudad():
    print("Modificarás un registro de la tabla Ciudades")
    getAllCiudades()
    IdUpdate = int(input("Id de la ciudad a modificar: "))
    result = []

    try:
        with connection.cursor() as cursor:
            sql = f"select * from ikea.ciudades where idCiudades = '{IdUpdate}'; "
            cursor.execute(sql)
            result = cursor.fetchall()
            registro = (result[0])
            user = str(registro['idCiudades'])
            nombre = registro['nombre']
            pais = str(registro['idPaises'])
             
            print("IdCiudad: " +  user + " Nombre: " + nombre + " País: " + pais )

            option = int(input("Actualizar nombre? 1-Si, 0-No"))
            if option == 1:
                print("Nombre actual: " + nombre)
                NuevoNombre = input("Nuevo nombre: ")
                nombre = NuevoNombre

            else:
                nombre = nombre

            option = int(input("Actualizar país? 1-Si, 0-No"))
            if option == 1:
                print("País actual: " + pais)
                getAllPaises()
                NuevoPais = int(input("Nuevo país: "))
                pais = NuevoPais

            else:
                pais = pais


            indicacion = f"UPDATE ikea.ciudades SET idCiudades = '{user}', nombre = '{nombre}', idPaises = '{pais}' where idCiudades = '{user}';"
            cursor.execute(indicacion)
            connection.commit()
            getAllCiudades()


    finally:
        pass

