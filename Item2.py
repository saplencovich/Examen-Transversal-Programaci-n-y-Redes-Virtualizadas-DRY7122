import requests


def obtener_coordenadas(ciudad):
  endpoint = "https://graphhopper.com/api/1/geocode"
  params = {
      "q": ciudad,
      "key": "c3d544e7-97e2-4d74-9da3-b43533978875"
  }
  response = requests.get(endpoint, params=params)
  data = response.json()
  return data["hits"][0]["point"]


def obtener_ruta(ciudad_origen, ciudad_destino, tipo_vehiculo):
 try:
     origen = obtener_coordenadas(ciudad_origen)
     destino = obtener_coordenadas(ciudad_destino)
     endpoint = "https://graphhopper.com/api/1/route"
     params = {
         "point": [f"{origen['lat']},{origen['lng']}", f"{destino['lat']},{destino['lng']}"],
         "vehicle": tipo_vehiculo,
         "locale": "es",
         "key": "c3d544e7-97e2-4d74-9da3-b43533978875"
     }
     response = requests.get(endpoint, params=params)
     data = response.json()
 
     if "paths" in data and len(data["paths"]) > 0:
         return data["paths"][0]
     else:
         print("No se encontró una ruta válida.")
         return None
 except Exception as e:
     print(f"Error al obtener la ruta: {e}")
     return None


def calcular_combustible(distancia_km):
  consumo_litros = distancia_km * 8 / 100
  return round(consumo_litros, 2)


def convertir_tiempo(segundos):
  horas = segundos // 3600
  minutos = (segundos % 3600) // 60
  segundos = segundos % 60
  return horas, minutos, segundos


def imprimir_resultados(ciudad_origen, ciudad_destino, distancia, duracion, combustible, ruta):
  horas, minutos, segundos = convertir_tiempo(duracion)
  print(f"Viaje desde {ciudad_origen} a {ciudad_destino}:")
  print(f"Distancia: {distancia:.2f} km")
  print(f"Duración: {horas} horas, {minutos} minutos, {segundos} segundos")
  print(f"Combustible requerido: {combustible:.2f} litros")
  print("Narrativa del viaje:")
  for step in ruta["instructions"]:
      print(step["text"])


def main():
 while True:
     print("=========================================================================")
     print("Menú:")
     print("1. Medir distancia entre Ciudad de Chile y Ciudad de Argentina")
     print("s. Salir")
     print("=========================================================================")
     opcion = input("Seleccione una opción: ")
     if opcion == "1":
         origen = input("Ingrese la Ciudad de Chile: ")
         destino = input("Ingrese la Ciudad de Argentina: ")
         print("==========================")
         print("1. Auto")
         print("2. Bicicleta")
         print("3. A pie")
         print("4. Motocicleta")
         print("5. Camión")
         print("==========================")
         tipo_vehiculo_esp = input("Ingrese el tipo de vehículo: ")
         if tipo_vehiculo_esp == "1":
            tipo_vehiculo = "car"
         elif tipo_vehiculo_esp == "2":
            tipo_vehiculo ="bike"
         elif tipo_vehiculo_esp == "3":
            tipo_vehiculo = "foot"
         elif tipo_vehiculo_esp == "4":
            tipo_vehiculo = "scooter"
         elif tipo_vehiculo_esp == "5":
            tipo_vehiculo = "truck"
         ruta = obtener_ruta(origen, destino, tipo_vehiculo)
         if ruta:
             distancia = ruta["distance"] / 1000
             duracion = ruta["time"] / 1000
             combustible = calcular_combustible(distancia)
             imprimir_resultados(origen, destino, distancia, duracion, combustible, ruta)
     elif opcion.lower() == "s":
         print("¡Hasta luego!")
         break
     else:
         print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
  main()