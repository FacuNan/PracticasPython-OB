import logging as lo
from getpass import getpass



nombreUsuario= input("Ingrse su nombre: ")

passwd = getpass("Ingrese su contraseña: ")

print(nombreUsuario, passwd)