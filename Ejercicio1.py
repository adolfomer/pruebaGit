"""
Pedir al usuario el numero de horas trabajadas y el coste por hora.
Mostrar por pantalla el "Sueldo" que le corresponde
"""

horas=int(input("Introduce el numero de horas trabajadas: "))
coste=int(input("Introduce el coste por hora en euros: "))
print("Su sueldo es: ", horas*coste, " euros.")

