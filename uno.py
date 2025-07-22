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


