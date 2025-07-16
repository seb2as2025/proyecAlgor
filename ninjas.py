def users(personajes):
    with open("Usuarios.txt", "w")as archivo:
        for per in personajes:
                archivo.write(f"{per['nombre']},{per['identificacion']},{per['edad']},{per[' correo']},{per['  contraseña']}\n")
        print("La información ha sido guardada en el archivo.")


def agregar(personajes):
    nombre=input("Ingrese El nombre del jugador: ")
    identificacion=int(input("Ingrese la identificacion: "))
    edad=int(input("Ingrese la edad: "))
    correo=input("Ingrese El correo: ")
    contraseña=input("Ingrese la contraseña(mínimo 8 caracteres, 1 mayúscula, 1 número): ")

    personajes.append({"nombre": nombre, "identificacion": identificacion, "edad": edad, "correo": correo, "contraseña": contraseña})
    print("Personaje registrado exitosamente.")


def buscar(personajes):
    if not personajes:
        print("No hay personajes para mostrar.")
        return
    ordenados = sorted(personajes, key=lambda p: p['nivel_poder'])
    print("\nLista de personajes ordenada por nivel de poder:")
    for per in ordenados:
        print(f"Nombre: {per['nombre']}, identificacion: {per['identificacion']}, edad: {per['edad']}, correo: {per['correo']}, contraseña: {per['contraseña']}")
    users(ordenados, "personajes_ordenados.txt")