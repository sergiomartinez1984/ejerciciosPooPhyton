'''Haz una clase llamada Persona que siga las siguientes condiciones:
Sus atributos son nombre, edad, DNI, sexo (H hombre, M mujer), peso y altura. No queremos
que se accedan directamente a ellos. Piensa que modificador de acceso es el más adecuado, también
su tipo. Si quieres añadir algún atributo puedes hacerlo.
Por defecto, todos los atributos menos el DNI serán valores por defecto según su tipo (0 números,
cadena vacía para String, etc.). Sexo sera mujer por defecto.
Se implantaran un constructor:
Un constructor con todos los atributos como parámetro.
Los métodos que se implementaran son:

calcularIMC(): calculara si la persona esta en su peso ideal (peso en kg/(altura^2 en m)),
devuelve un -1 si esta por debajo de su peso ideal, un 0 si esta en su peso ideal y un 1 si tiene
sobrepeso . También devuelve el IMC.

esMayorDeEdad(): indica si es mayor de edad, devuelve un booleano.

introducirSexo(char sexo): introducido el sexo. Si no es correcto, sera M. No sera visible al
exterior.

toString(): devuelve toda la información del objeto.

generaDNI(): genera un numero aleatorio de 8 cifras, genera a partir de este su número su letra
correspondiente. Este método sera invocado cuando se construya el objeto.
Métodos de cada parámetro, excepto de DNI.

Ahora,Pide por teclado el nombre, la edad, sexo, peso y altura.

Crea 3 objetos de la clase anterior, el primer objeto obtendrá las anteriores variables pedidas por
teclado, el segundo objeto obtendrá todos los anteriores menos el peso y la altura y el último los
datos por defecto, para este último utiliza los métodos set para darle a los atributos un valor.
Para cada objeto, deberá comprobar si esta en su peso ideal, tiene sobrepeso o por debajo de su·
peso ideal con un mensaje.
Indicar para cada objeto si es mayor de edad.
Por último, mostrar la información de cada objeto.'''

from self import self
import random

class Personas():
    def __init__(self, nombre = ' ', edad = 0, dni = ' ', sexo = 'mujer', peso = 0, altura = 0,):
                self.nombre = nombre
                self.edad = edad
                self.dni = dni
                self.sexo = sexo
                self.peso = peso
                self.altura = altura


    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_dni(self):
        return self.dni

    def get_sexo(self):
        return self.sexo

    def get_peso(self):
        return self.peso

    def get_altura(self):
        return self.altura

    def set_nombre(self):
        return self.nombre

    def set_edad(self):
        return self.edad

    def set_dni(self):
        return self.dni

    def set_sexo(self):
        return self.sexo

    def set_peso(self):
        return self.peso

    def set_altura(self):
        return self.altura

    def __str__(self):
        return "Nombre: " + str(self.nombre) + ", Edad: " + \
                str(self.edad) + ", DNI: " + str(self.dni) + ", Sexo: " + \
                    str(self.sexo) + ", Peso: " + str(self.peso) + ", Altura(cm): " + str(self.altura)


    def esMayorDeEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    def introducirSexo(self, sexo):
        if sexo != 'M' or sexo != 'H':
            self.sexo = 'M'
        else:
            self.sexo = sexo

    def calcularIMC(self,peso,altura):

        imc = peso/(altura*altura)

        if(imc < 18.5):
            print('\n usted esta por debajo de su peso')
        if(imc > 18.5 and imc < 24.9):
            print('\n usted tiene un peso ideal')
        if(imc > 24.9):
            print('\n usted tiene sobrepeso')

        print('su IMC es de : {}'.format(imc))


    def mayorDeEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False


    def introducirSexo(sexo):
        if sexo != 'M' or sexo != 'H':
            self.sexo = 'M'
        else:
            return sexo

    def generarElDNI(dni):
        num = random.randrange(10000000, 99999999)
        letraDni = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
        letra = letraDni[num % 23]
        dni = repr(num) + letra
        return dni

