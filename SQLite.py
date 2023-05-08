import sqlite3
import getpass


def main():
    menu = int(input("¿Que deseas hacer? 1.Ver lista 2.Añadir usuario 3.login 4.Eliminar usuario 0. Para salir"))
    while menu != 0:
        if menu == 1:
            traer_lista()
            menu = int(input("¿Que deseas hacer? 1.Ver lista 2.Añadir usuario 3.login 4.Eliminar usuario "))
        elif menu==2:
            id= int(input("Ingrese numero de identificacion: "))
            username = input("Ingrese su nombre: ")
            password = getpass.getpass("Contraseña: ")
            crear_usuario(id, username, password)
            traer_lista()
            print("Usuario creado con exito")
            menu = int(input("¿Que deseas hacer? 1.Ver lista 2.Añadir usuario 3.login 4.Eliminar usuario "))
        elif menu == 3:
            username = input("ingrese su nombre: ")
            password= getpass.getpass("Contraseña: ")
            if verifica_credenciales(username, password):
                print('Bien Hecho')
            else:
                print(' Lo siento ')
            menu = int(input("¿Que deseas hacer? 1.Ver lista 2.Añadir usuario 3.login 4.Eliminar usuario "))
        elif menu == 4:
            nombre = input("¿Que usuario deseas eliminar? ingresa su nombre: ")

            eliminar(nombre)
            print("Usuario eliminado con exito")
            menu = int(input("¿Que deseas hacer? 1.Ver lista 2.Añadir usuario 3.login 4.Eliminar usuario "))
        else:
            print("Lo siento la opcion es incorrecta")
            menu = int(input("¿Que deseas hacer? 1.Ver lista 2.Añadir usuario 3.login 4.Eliminar usuario "))
    print("Muchas gracias por visitarnos")




def verifica_credenciales(username, password):
    conn = sqlite3.connect('mifichero.db')

    cursor = conn.cursor()

    query = f"SELECT id FROM users WHERE nombre = '{username}' AND password = '{password}'"
    rows = cursor.execute(query)
    data = rows.fetchone()

    cursor.close()
    # Cerrar la conexión
    conn.close()

    if data == None:
        return False
    return True



def crear_usuario(identificador, username, password):
    conn = sqlite3.connect('mifichero.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users(id, nombre, password) VALUES ({identificador}, '{username}', '{password}')"

    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

def traer_lista():
    conn = sqlite3.connect('mifichero.db')
    cursor = conn.cursor()

    query = "SELECT * FROM users"
    rows = cursor.execute(query)
    for row in rows:
        print(row)

    cursor.close()
    conn.close()

def eliminar(username):
    conn = sqlite3.connect('mifichero.db')
    cursor = conn.cursor()

    query = f"DELETE FROM users WHERE nombre == '{username}'"

    cursor.execute(query)

    conn.commit()
    cursor.close()
    conn.close()



if __name__ == '__main__':
    main()