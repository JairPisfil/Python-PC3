def get_fuel_percentage():
    while True:
        try:
            fraction = input("Ingrese una fracción (X/Y): ")
            x_str, y_str = fraction.split("/")
            x = int(x_str)
            y = int(y_str)

            if y == 0:
                raise ZeroDivisionError("El denominador no puede ser 0.")
            if x > y:
                raise ValueError("El numerador no puede ser mayor que el denominador.")

            porcentaje = round((x / y) * 100)

            if porcentaje <= 1:
                print("E")
            elif porcentaje >= 99:
                print("F")
            else:
                print(f"{porcentaje}%")
            break

        except ValueError:
            print("Error: Ingrese solo números enteros válidos en formato X/Y y asegúrese que X ≤ Y.")
        except ZeroDivisionError:
            print("Error: El denominador no puede ser 0.")

get_fuel_percentage()