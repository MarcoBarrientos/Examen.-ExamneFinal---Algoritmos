nombre_estudiante = input("Ingrese el nombre del estudiante: ")
notas = []

for i in range(4):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {i + 1}: "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("La nota debe estar en el rango de 0 a 10.")
        except ValueError:
            print("Ingrese un número válido.")

promedio = sum(notas) / len(notas)

with open("notas.txt", "a") as archivo:
    archivo.write(f"Nombre del estudiante: {nombre_estudiante}\n")
    archivo.write("Notas: " + ", ".join(map(str, notas)) + "\n")
    archivo.write(f"Promedio: {promedio}\n\n")

print("Datos guardados en el archivo 'notas.txt'.")
