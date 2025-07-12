import requests
import zipfile
import os

url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop"
nombre_imagen = "imagen.jpg"

try:
    response = requests.get(url)
    response.raise_for_status()

    with open(nombre_imagen, "wb") as f:
        f.write(response.content)
    print("✅ Imagen descargada correctamente.")
except requests.RequestException as e:
    print("❌ Error al descargar la imagen:", e)

zip_name = "imagen.zip"
with zipfile.ZipFile(zip_name, "w") as zipf:
    zipf.write(nombre_imagen)
print("✅ Imagen comprimida en:", zip_name)

directorio_destino = "descomprimido"
os.makedirs(directorio_destino, exist_ok=True)

with zipfile.ZipFile(zip_name, "r") as zipf:
    zipf.extractall(directorio_destino)
print("✅ Imagen descomprimida en carpeta:", directorio_destino)