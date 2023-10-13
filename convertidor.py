import temperatura
import masa
import tiempo

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen == "Celsius" and unidad_destino == "Fahrenheit":
        return temperatura.celsius_a_fahrenheit(valor)
    elif unidad_origen == "Celsius" and unidad_destino == "Kelvin":
        return temperatura.celsius_a_kelvin(valor)
    elif unidad_origen == "Fahrenheit" and unidad_destino == "Celsius":
        return temperatura.fahrenheit_a_celsius(valor)
    elif unidad_origen == "Fahrenheit" and unidad_destino == "Kelvin":
        return temperatura.fahrenheit_a_kelvin(valor)
    elif unidad_origen == "Kelvin" and unidad_destino == "Celsius":
        return temperatura.kelvin_a_celsius(valor)
    elif unidad_origen == "Kelvin" and unidad_destino == "Fahrenheit":
        return temperatura.kelvin_a_fahrenheit(valor)
    else:
        return None

def convertir_masa(valor, unidad_origen, unidad_destino):
    if unidad_origen == "Kilogramo" and unidad_destino == "Gramo":
        return masa.kilogram_a_gram(valor)
    elif unidad_origen == "Kilogramo" and unidad_destino == "Tonelada":
        return masa.kilogram_a_ton(valor)
    elif unidad_origen == "Gramo" and unidad_destino == "Kilogramo":
        return masa.gram_a_kilogram(valor)
    elif unidad_origen == "Gramo" and unidad_destino == "Tonelada":
        return masa.gram_a_ton(valor)
    elif unidad_origen == "Tonelada" and unidad_destino == "Kilogramo":
        return masa.ton_a_kilogram(valor)