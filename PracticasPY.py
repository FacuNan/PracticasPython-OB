def nombre(nombre):
    print(f"hola {nombre}")

nombre("Facundo")

def coche(**kwargs):
    if kwargs['coche']=='bonito':
        print("Tu coche es bonito")

coche(coche="feo")

anonima = lambda: print("hola")

anonima()


sumatoria = lambda x: x+x

print(sumatoria(2))