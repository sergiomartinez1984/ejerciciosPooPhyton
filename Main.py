

from Personas import Personas

print("introduce tu nombre")
nombre = input()
print("introduce tu edad")
edad = int(input())
print("introduce tu sexo")
sexo = input()
print("introduce tu peso")
peso = float(input())
print("introduce tu altura")
altura = float(input())

dni = ''

persona1 = Personas(nombre, edad, Personas.generarElDNI(dni), sexo,peso,altura)

persona2 = Personas(nombre, edad, Personas.generarElDNI(dni), sexo)

persona3 = Personas()

print(persona1.calcularIMC(peso,altura))

print(persona2)

print(persona3)
