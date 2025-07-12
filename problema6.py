import requests

def obtener_datos_tipo_cambio():
    resultados = []

    for mes in range(1, 13): 
        try:
            url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?month={mes}&year=2025"
            respuesta = requests.get(url)
            respuesta.raise_for_status()
            datos = respuesta.json()

            for entry in datos:
                fecha = entry["fecha"]
                compra = float(entry["compra"])
                venta = float(entry["venta"])
                diferencia = venta - compra

                resultados.append({
                    "fecha": fecha,
                    "compra": compra,
                    "venta": venta,
                    "diferencia": diferencia
                })

        except requests.RequestException as e:
            print(f"Error al obtener datos del mes {mes}: {e}")

    return resultados

def analizar_tipo_cambio(datos):
    if not datos:
        print("No hay datos disponibles.")
        return

    min_compra = min(d["compra"] for d in datos)
    fechas_min_compra = [d["fecha"] for d in datos if d["compra"] == min_compra]

    max_venta = max(d["venta"] for d in datos)
    fechas_max_venta = [d["fecha"] for d in datos if d["venta"] == max_venta]

    max_diferencia = max(d["diferencia"] for d in datos)
    fechas_max_dif = [d["fecha"] for d in datos if d["diferencia"] == max_diferencia]

    print("\n📉 Fechas con valor de COMPRA mínimo:")
    print(f"Compra mínima: {min_compra}")
    print(fechas_min_compra)

    print("\n📈 Fechas con valor de VENTA máximo:")
    print(f"Venta máxima: {max_venta}")
    print(fechas_max_venta)

    print("\n🔁 Fechas con mayor DIFERENCIA entre venta y compra:")
    print(f"Diferencia máxima: {max_diferencia}")
    print(fechas_max_dif)

datos_cambio = obtener_datos_tipo_cambio()
analizar_tipo_cambio(datos_cambio)