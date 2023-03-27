from AppAscenzi.models import Juguete


for _ in range(0,5):
    Juguete(nombre="Nombre de empresa", 
    tamaño="tamaño",
    color="color",
    marca="marca",
    cantidad= "cantidad",
    categoria= "categoria",
    ).save()

