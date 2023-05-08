import operaciones
import sys
sys.path.append("/home/facundo/Escritorio/saluda/")
import saluda

def main():
    res = operaciones.resta(2,2)
    print("Hola desde la main", res)
    saluda.saluda("Facundo")

if __name__== '__main__':
    main()