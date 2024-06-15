# Proyecto 3: Lista de Tareas
# Descripción: Una aplicación para gestionar tareas,
# donde se pueden agregar, eliminar y ver las tareas pendientes.

tareas = []

def agregar_tarea():
    tarea = input("Ingresa la tarea: ")
    tareas.append(tarea)
    print("Tarea agregada.")

def eliminar_tarea():
    tarea = input("Ingresa la tarea a eliminar: ")
    if tarea in tareas:
        tareas.remove(tarea)
        print("Tarea eliminada.")
    else:
        print("Tarea no encontrada.")

def mostrar_tareas():
    print("Lista de tareas:")
    for tarea in tareas:
        print(f"- {tarea}")

def menu():
    while True:
        print("\nMenú:")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Ver tareas")
        print("4. Salir")
        
        eleccion = input("Elige una opción: ")
        
        if eleccion == '1':
            agregar_tarea()
        elif eleccion == '2':
            eliminar_tarea()
        elif eleccion == '3':
            mostrar_tareas()
        elif eleccion == '4':
            break
        else:
            print("Opción no válida")

menu()
