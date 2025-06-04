#Simulador de cajero automatico en python

import time
class CajeroAutomatico:
    def __init__(self):
        self.saldo = 5000.00
        self.historial = []
        self.sesion_activa = False
        self.pin_correcto = None 

    def registrar_pin(self):
        print("Bienvenido. Debes registrar un PIN de 4 dígitos.")
        while True:
            pin = input("Ingresa tu nuevo PIN (4 dígitos numéricos): ")
            if self.validar_pin(pin):
                self.pin_correcto = pin
                print("PIN registrado exitosamente.")
                break
            else:
                print("El PIN debe tener exactamente 4 dígitos numéricos. Intenta de nuevo.")

    def validar_pin(self, pin):
        return len(pin) == 4 and pin.isdigit()

    def verificar_pin(self, pin):
        if pin == self.pin_correcto:
            self.sesion_activa = True
            print("PIN correcto. Acceso concedido.")
            return True
        else:
            print("PIN incorrecto. Intenta de nuevo.")
            return False

    def consultar_saldo(self):
        if self.sesion_activa:
            print(f"Saldo actual: ${self.saldo:.2f}")
            self.historial.append(f"Consulta de saldo: ${self.saldo:.2f}")
        else:
            print("Por favor, inicia sesión primero.")

    def depositar(self, monto):
        if self.sesion_activa:
            if monto > 0:
                self.saldo += monto
                print(f"Depósito exitoso. Nuevo saldo: ${self.saldo:.2f}")
                self.historial.append(f"Depósito: ${monto:.2f}")
            else:
                print("El monto debe ser mayor a 0.")
        else:
            print("Por favor, inicia sesión primero.")

    def retirar(self, monto):
        if self.sesion_activa:
            if monto > 0:
                if monto <= self.saldo:
                    self.saldo -= monto
                    print(f"Retiro exitoso. Nuevo saldo: ${self.saldo:.2f}")
                    self.historial.append(f"Retiro: ${monto:.2f}")
                else:
                    print("Fondos insuficientes.")
            else:
                print("El monto debe ser mayor a 0.")
        else:
            print("Por favor, inicia sesión primero.")

    def ver_historial(self):
        if self.sesion_activa:
            if self.historial:
                print("\nHistorial de transacciones:")
                for transaccion in self.historial:
                    print(transaccion)
            else:
                print("No hay transacciones registradas.")
        else:
            print("Por favor, inicia sesión primero.")

    def cerrar_sesion(self):
        print("Cerrando sesión...")
        time.sleep(2) 
        self.sesion_activa = False
        print("Sesión cerrada.")

def main():
    cajero = CajeroAutomatico()

    if cajero.pin_correcto is None:
        cajero.registrar_pin()

    intentos = 3
    while intentos > 0:
        pin = input("Ingresa tu PIN: ")
        if cajero.verificar_pin(pin):
            break
        intentos -= 1
        print(f"Te quedan {intentos} intentos.")
    
    if not cajero.sesion_activa:
        print("Demasiados intentos fallidos. Acceso bloqueado.")
        return

    while cajero.sesion_activa:
        print("\n=== Menú Cajero Automático ===")
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Ver historial de transacciones")
        print("5. Salir")
        
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            cajero.consultar_saldo()
        elif opcion == "2":
            try:
                monto = float(input("Ingresa el monto a depositar: $"))
                cajero.depositar(monto)
            except ValueError:
                print("Por favor, ingresa un monto válido.")
        elif opcion == "3":
            try:
                monto = float(input("Ingresa el monto a retirar: $"))
                cajero.retirar(monto)
            except ValueError:
                print("Por favor, ingresa un monto válido.")
        elif opcion == "4":
            cajero.ver_historial()
        elif opcion == "5":
            cajero.cerrar_sesion()
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()