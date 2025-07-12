def obtener_calificaciones():
    entrada = input("Ingrese las calificaciones separadas por comas: ")
    calificaciones_str = entrada.split(",")
    calificaciones = []

    for valor in calificaciones_str:
        try:
            nota = int(valor.strip())
            calificaciones.append(nota)
        except ValueError:
            print(f"'{valor}' no es una calificación válida. Asegúrese de ingresar solo números.")
            return  # Finaliza si hay error

    print("Calificaciones registradas:", calificaciones)

obtener_calificaciones()