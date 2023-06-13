#Ejercicio 1
def contar_palabra(vector, palabra):
    if not vector:
        return 0
    count = 1 if vector[0] == palabra else 0
    return count + contar_palabra(vector[1:], palabra)
vector_palabras = ["Miki", "mundo", "Miki", "abejitas", "chocolate", "helado"]
palabra_a_contar = "Miki"
resultado = contar_palabra(vector_palabras, palabra_a_contar)
print(f"La palabra '{palabra_a_contar}' aparece {resultado} veces.")
