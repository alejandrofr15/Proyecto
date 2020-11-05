#Conexión a Servidor
#connection = pymysql.connect(
#    host = "localhost",
#    user = "root",
#    passwd = "tuContraseña",
#    db= "ikea",
#    cursorclass = pymysql.cursors.DictCursor,
#)


#Obtener todos los registros de una tabla
#def getAllClients():
#    result = {}
#    try:
#        with connection.cursor() as cursor:
#            sql = "SELECT * FROM ikea.<tabla>;"
#            cursor.execute(sql)
#            result = cursor.fetchall()
#    finally:
#        table = PrettyTable()
#        table.field_names = ["campo1", "campo2", "campo3", "campo4", "campo5", "campo6", "campo7" ...]
#       for cliente in result:
#            table.add_row([cliente["campo1"], cliente["campo2"], cliente["campo3"], cliente["campo4"], cliente["campo5"], cliente["campo6"], cliente["campo7"] ...])
#        print(table)


#Agregar un nuevo registro a una tabla
#def addNewClient():
#    print("Añadirás un nuevo cliente")
#    var1 = input("Campo1: ")
#    var2 = input("Campo2: ")
#    var3 = input("Campo3: ")
#    var4 = input("Campo4")
#    var5 = input("Campo5: ")
#    var6 = input("Campo6: ")
#    var7 = input("Campo7: ")
#    var8 = input("Campo8: ")

#    try:
#        with connection.cursor() as cursor:
#            sql = f"insert into ikea.<tabla> (campo1, campo2, campo3, campo4, campo5, campo6, campo7, campo8) values ('{var1}','{var2}','{var3}','{var4}','{var5}','{var6}','{var7}','{var8}');"
#            cursor.execute(sql)
#            connection.commit()

#    finally:
#        getAllClients()



#Borrar un registro
#def deleteClient():
#    result = []
#    print("Borrarás un registro de la tabla usuarios")
#    idDel = int(input("Id del usuario a borrar: "))

#    try:
#        with connection.cursor() as cursor:
#            sql = f"select <campo1, campo2, campo3, campo4> from ikea.<tabla> where id<tabla> = {idDel}; " (Campos = Campos para verificar si el usuario desea eliminar este registro)
#            indicacion = f"delete from ikea.<tabla> where id<tabla> = {idDel};"
            #cursor.execute(sql)
            #result = cursor.fetchall()
            #registro = (result[0])
            #datosReg = str(registro['campo1']) + " " + registro['campo2'] + " " + registro['campo3'] + " " + registro['campo4']
            #print(datosReg)
            #print("Borrarás definitivamente el registro anterior. Estás seguro?")
            #opcion = int(input("Si(1), No(0). Escribe 1 o 0."))

#            if opcion == 1:
#                cursor.execute(indicacion)
#                connection.commit()
#                print("Se ha borrado definitivamente el registro: " + datosReg)
#                getAllClients()

#            else:
#                pass


#    finally:
#        pass


#Modificar un registro
#def updateUsuario():
#    print("Modificarás un registro de la tabla Usuarios")
#    getAllUsuarios()
#    IdUpdate = int(input("Id del usuario a modificar: "))
#    result = []

#    try:
#        with connection.cursor() as cursor:
#            sql = f"select * from ikea.<tabla> where id<tabla> = '{IdUpdate}'; "
#            cursor.execute(sql)
#            result = cursor.fetchall()
#            registro = (result[0])
#            user = str(registro['id<tabla>'])
#            var1 = registro['campo1']
#            var2 = registro['campo2']
#            var3 = registro['campo3']
#            var4 = registro['campo4']
#            var5 = registro['campo5']
#            var6 = registro['campo6']
#            var7 = registro['campo7']
#            var8 = registro['campo8'] 
#            datosReg = user + " " + var1 + " " + var2 + " " + var3 + " " + var4 + " " + var5 + " " + var6 + " " + var7 + " " + var8
#            print(datosReg)

#            option = int(input("Actualizar campo1? 1-Si, 0-No"))
#            if option == 1:
#                print("campo1 actual: " + var1)
#                NewVar1 = input("Nueva var1: ")
#                var1 = NewVar1

#            else:
#                var1 = var1

#            Repetir para todos los campos.


#            indicacion = f"UPDATE ikea.usuarios SET idUsuarios = '{user}', campo1 = '{var1}', campo2 = '{var2}', campo3 = '{var3}', campo4 = '{var4}', ... where id<tabla> = idUpdate;"
#            cursor.execute(indicacion)
#            connection.commit()
#            getAllUsuarios()


#    finally:
#        pass
