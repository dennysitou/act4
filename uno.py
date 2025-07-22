#simulador de votacion
name = input("Ingresa tu nombre: ")
longname = len(name)
dpi = input("Ingresa tu dpi: ")
longdpi = len(dpi)
departament = input("Ingresa tu departamento: ").lower()
born = int(input("Ingresa tu año de nacimiento: "))

anio = 2025
edad = anio - born
print(f"Su edad es: {edad}")

if longname < 5:
    print("El nombre debe tener mas de 5 letras")

if longdpi < 13:
    print("el dpi debe tener 13 digitos")
    exit()

canvote = False
depas = ["peten", "alta verapaz"]

if edad >= 18:
    canvote = True

elif (departament in depas):
    canvote = True
    print("puede votar desde los 17 años")

if canvote:
    print(f"Bienvenido, {name}. Su centro de votacion esta en {departament} ")
else:
    print("No puedes votar")
