#Ejercicio 3
class PilaBitacora:
    def __init__(self):
        self.pila = []

    def agregar_mision(self, planeta, captura, recompensa):
        mision = {"planeta": planeta, "captura": captura, "recompensa": recompensa}
        self.pila.append(mision)

    def obtener_planetas_visitados(self):
        return [mision["planeta"] for mision in self.pila]

    def calcular_total_creditos(self):
        return sum(mision["recompensa"] for mision in self.pila)

    def encontrar_mision_captura(self, objetivo):
        for i, mision in enumerate(self.pila, 1):
            if mision["captura"] == objetivo:
                return i, mision["planeta"]
        return None, None
bitacora = PilaBitacora()
bitacora.agregar_mision("Tatooine", "Jabba el Hutt", 1000)
bitacora.agregar_mision("Coruscant", "Greedo", 500)
bitacora.agregar_mision("Bespin", "Lando Calrissian", 800)
bitacora.agregar_mision("Endor", "Wicket W. Warrick", 300)
bitacora.agregar_mision("Hoth", "Han Solo", 2000)
bitacora.agregar_mision ("Kashyyyk","Chewbacca",  1500)
bitacora.agregar_mision("Naboo", "Jar Jar Binks", 400)
bitacora.agregar_mision("Mustafar", "Darth Vader",  2500)

# a)
planetas_visitados = bitacora.obtener_planetas_visitados()
print("Planetas visitados en orden:")
print('\n'.join(planetas_visitados))

# b)
total_creditos = bitacora.calcular_total_creditos()
print("Total de créditos galácticos recaudados:", total_creditos)

# c)
han_solo_mision, planeta_captura = bitacora.encontrar_mision_captura("Han Solo")
print("Número de la misión en la que capturó a Han Solo:", han_solo_mision)
print("Planeta de la captura de Han Solo:", planeta_captura)
