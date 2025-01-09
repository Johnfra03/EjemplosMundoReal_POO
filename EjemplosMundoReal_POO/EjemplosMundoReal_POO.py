# Clase para representar una cuenta bancaria
class CuentaBancaria:
    def __init__(self, nombre_cliente, saldo_inicial):
        """
        Constructor de la clase CuentaBancaria.

        :param nombre_cliente: Nombre del titular de la cuenta.
        :param saldo_inicial: Saldo inicial de la cuenta.
        """
        self.nombre_cliente = nombre_cliente  # Nombre del titular de la cuenta
        self.saldo_actual = saldo_inicial  # El saldo inicial de la cuenta

    def depositar(self, cantidad):
        """
        Método para depositar dinero en la cuenta.

        :param cantidad: Monto a depositar en la cuenta.
        """
        if cantidad > 0:
            self.saldo_actual += cantidad  # Se suma la cantidad al saldo
            print(f"Se han depositado ${cantidad}. El saldo actual es ${self.saldo_actual}.")
        else:
            print("El monto a depositar debe ser mayor que 0.")

    def retirar(self, cantidad):
        """
        Método para retirar dinero de la cuenta.

        :param cantidad: Monto a retirar de la cuenta.
        """
        if cantidad > 0:
            if cantidad <= self.saldo_actual:
                self.saldo_actual -= cantidad  # Se resta la cantidad al saldo
                print(f"Se han retirado ${cantidad}. El saldo actual es ${self.saldo_actual}.")
            else:
                print("Saldo insuficiente para realizar el retiro.")
        else:
            print("El monto a retirar debe ser mayor que 0.")

    def mostrar_saldo(self):
        """
        Muestra el saldo actual de la cuenta.
        """
        print(f"El saldo de la cuenta de {self.nombre_cliente} es ${self.saldo_actual}.")

if __name__ == "__main__":
    # Crear una cuenta bancaria con saldo inicial de 1000
    cuenta_cliente = CuentaBancaria("John Franco", 5000)

    # Mostrar el saldo inicial
    cuenta_cliente.mostrar_saldo()

    # Depositar 600 en la cuenta
    cuenta_cliente.depositar(600)

    # Intentar retirar 300 de la cuenta
    cuenta_cliente.retirar(300)

    # Intentar retirar más de lo que hay en la cuenta
    cuenta_cliente.retirar(20000)

    # Mostrar el saldo final
    cuenta_cliente.mostrar_saldo()
