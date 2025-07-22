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
    print("No puedes votar.")



#SALARIO

salary = float(input("Ingrese su salario: "))
dependents = int(input("Ingrese el numero de dependientes: "))

if salary < 40000 and dependents > 2:
    print("No paga impuestos")
else:
    if 0 <= salary <= 30000:
        print("Paga el 5%")
    elif 30001 <= salary <= 60000:
        print("Paga el 10%")
    elif 60001 <= salary <= 100000:
        print("Paga el 15%")
    elif salary > 100000:
        print("Paga el 20%")

    print("La deduccion por dependientes es de:  ", dependents * 1000)



#penalizacion
valid_users = {"admin123", "chepito22", "emebd"}
intentos = 3
acceso = False

while intentos > 0:
    password = input("Ingrese su password: ")
    if password in valid_users:
        acceso = True
        break
    else:
        intentos -= 1
        if intentos > 0:
            print(f"le quedan {intentos} intentos")
        else:
            print("Acceso bloqueado")

if acceso:
    print("Menu de opciones")
    print("1. Ver perfil")
    print("2. Cambiar contraseña")
    print("3. Cerrar sesion")

#factuacion
productos = []
while True:
    precio = input("Ingrese el precio del producto o escriba fin para terminar: ")
    if precio.lower() == 'fin':
        break
    precio_float = float(precio)
    productos.append(precio_float)

subtotal = sum(productos)

propina = 0
if input("Desea dejar propina? si/no").lower() == 'si':
    propina = float(input("Que % desea dejar? "))

descuento = 0
if input("Tiene tarjeta de credito? si/no").lower() == 'si':
    descuento = 10

iva =  subtotal * 0.12
propina1 = subtotal * (propina / 100)
descuento1 = subtotal * (descuento / 100)
total = subtotal + iva + propina - descuento


print(f"Subtotal: Q{subtotal}")
print(f"IVA (12%): Q{iva}")
print(f"Propina: Q{propina1:}")
print(f"Descuento: Q{descuento1}")

print(f"Total: Q{total}")

#fechas
day = int(input("Ingrese el día del mes: "))
month = int(input("Ingrese el mes del año: "))
year = int(input("Ingrese el año: "))
validate = True

if month in [4, 6, 9, 11] and day > 30:
    validate = False
    print("Este mes solo tiene 30 días")
elif month == 2:
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        maxdias = 29
    else:
        maxdias = 28
    if day > maxdias:
        validate = False
        print(f"Febrero de {year} solo tiene {maxdias} días")

if validate:
    print(f"La fecha es: {day}/{month}/{year}")

    if month < 3:
        m = month + 12
        adjusted_year = year - 1
    else:
        m = month
        adjusted_year = year

    k = day
    D = adjusted_year % 100
    C = adjusted_year // 100

    d = (k + (13 * (m + 1)) // 5 + D + D // 4 + C // 4 - 2 * C) % 7

    dias_semana = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]

    print(f"El día de la semana es: {dias_semana[d]}")
else:
    print("Fecha invalida")

#precioyviaje
weight = float(input("Ingrese el peso del paquete en kilogramos: "))
dist = float(input("Ingrese la distancia en kilómetros: "))
urgencia = input("¿Urgente? (si/no): ").lower()
tamanio = input("Tamaño del paquete? (pequeño/mediano/grande): ").lower()

preciopeso = weight * 10
preciodist = dist * 10
baseprice = preciopeso + preciodist

recargourgencia = 0
recargotamanio = 0
descuento = 0

if urgencia == "si":
    recargo_urgencia = 50
    baseprice += recargourgencia

if tamanio == "grande":
    recargo_tamanio = 30
    baseprice += recargotamanio

if urgencia == "no" and weight < 5:
    descuento = 20
    baseprice -= descuento

#desglose
print(f"Costo por peso: {weight} kg x Q10: {preciopeso}")
print(f"Costo por distancia: {dist} km x Q10: {preciodist}")
print(f"Subtotal: Q{preciopeso + preciodist}")

if recargourgencia > 0:
    print(f"Recargo por urgencia: {recargourgencia}")

if recargotamanio > 0:
    print(f"Recargo por urgencia: {recargotamanio}")

if descuento > 0:
    print(f"Descuento (No urgente y menor a 5kg de peso: {descuento}")

print(f"Total a pagar: {baseprice}")



#calificacionesconcurva

#coordenadas

#promocionescine
edadd = int(input("Ingrese su edad: "))
dweek = input("Ingrese el día de la semana: ").lower()
est = input("Es estudiante? si/no: ").lower() == "si"
miercoles = dweek == "miércoles" or dweek == "miercoles"

if edadd < 13:
    print("No puede ver peliculas de mayores de 15 años")
    exit()

if est:
    preciobase = 35
else:
    preciobase = 50

if miercoles:
    preciofinal = preciobase
    promocion = "Promocion 2x1 aplicada"
else:
    preciofinal = preciobase
    promocion = "No promocion disponible"


print("Precio final a pagar: ", preciofinal)




