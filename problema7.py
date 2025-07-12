from pyfiglet import Figlet
import random

figlet = Figlet()

fuentes = figlet.getFonts()

fuente = input("Ingrese una fuente (Enter para aleatoria): ").strip()

if fuente not in fuentes:
    fuente = random.choice(fuentes)
    print(f"Fuente aleatoria seleccionada: {fuente}")

figlet.setFont(font=fuente)

texto = input("Ingrese el texto a imprimir: ")

print(f"figlet.renderText(texto)")