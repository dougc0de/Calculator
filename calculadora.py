class calculadora:
    def valores(self):
        self.valor1 = int(input('Ingrese el valor 1:  '))
        self.valor2 = int(input('Ingrese el valor 2:  '))

    def suma(self):
        self.valores()
        operacionSuma = self.valor1 + self.valor2
        print(f'\n****La suma es igual a {operacionSuma}')

    def resta(self):
        self.valores()
        operacionresta = self.valor1 - self.valor2
        print(f'\n****La resta es igual a {operacionresta}')

    def multi(self):
        self.valores()
        operacionmulti = self.valor1 * self.valor2
        print(f'\n****La multiplicacion es igual a {operacionmulti}')

    def div(self):
        self.valores()
        operaciondiv = self.valor1 / self.valor2
        print(f'\n****La division es igual a {operaciondiv}')


print('Bienvenido a la Calculadora.')
while True:
    opc = int(input('\nColoque el numero segun la operacion que se quiere realizar. \n1.Suma \n2.Resta \n3.Multiplicacion \n4.Division \nOperacion a realizar:  '))

    operacion = calculadora()

    if opc == 1:
        operacion.suma()

    elif opc == 2:
        operacion.resta()

    elif opc == 3:
        operacion.multi()

    elif opc == 4:
        operacion.div()

    elif opc == 5:
        print('Saliendo. Adios!')
        break

    else:
        print('Opcion no valida')
