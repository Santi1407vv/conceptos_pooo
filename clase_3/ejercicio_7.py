class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance


propietarios = ["Juan Pérez", "María García"]
cuenta = CuentaBancaria("123456789", propietarios, 1500.0)

print("Número de cuenta:", cuenta.numero_cuenta)
print("Propietarios:", cuenta.propietarios)
print("Balance:", cuenta.balance)
#8---------------------------------------------------------------------
class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            return True
        else:
            return False


propietarios = ["Juan Pérez", "María García"]
cuenta = CuentaBancaria("123456789", propietarios, 1500.0)

print("Saldo inicial:", cuenta.balance)

if cuenta.depositar(500):
    print("Depósito exitoso. Saldo actual:", cuenta.balance)
else:
    print("Depósito fallido. La cantidad debe ser mayor que cero.")

if cuenta.depositar(-200):
    print("Depósito exitoso. Saldo actual:", cuenta.balance)
else:
    print("Depósito fallido. La cantidad debe ser mayor que cero.")
#9--------------------------------------
class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            return True
        else:
            return False

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.balance:
            self.balance -= cantidad
            return True
        else:
            return False


propietarios = ["Juan Pérez", "María García"]
cuenta = CuentaBancaria("123456789", propietarios, 1500.0)

print("Saldo inicial:", cuenta.balance)

if cuenta.retirar(200):
    print("Retiro exitoso. Saldo actual:", cuenta.balance)
else:
    print("Retiro fallido. Fondos insuficientes o cantidad inválida.")

if cuenta.retirar(1800):
    print("Retiro exitoso. Saldo actual:", cuenta.balance)
else:
    print("Retiro fallido. Fondos insuficientes o cantidad inválida.")
#10---------------------------------------------
class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            return True
        else:
            return False

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.balance:
            self.balance -= cantidad
            return True
        else:
            return False

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        return cuota


propietarios = ["Juan Pérez", "María García"]
cuenta = CuentaBancaria("123456789", propietarios, 1500.0)

print("Saldo inicial:", cuenta.balance)

cuota = cuenta.aplicar_cuota_manejo()
print(f"Se aplicó una cuota de manejo de: {cuota}. Saldo actual: {cuenta.balance}")

if cuenta.retirar(200):
    print("Retiro exitoso. Saldo actual:", cuenta.balance)
else:
    print("Retiro fallido. Fondos insuficientes o cantidad inválida.")
#11---------------------------------------------------
class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            return True
        else:
            return False

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.balance:
            self.balance -= cantidad
            return True
        else:
            return False

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        return cuota

    def mostrar_detalles(self):
        print("Número de cuenta:", self.numero_cuenta)
        print("Propietarios:", self.propietarios)
        print("Saldo:", self.balance)


propietarios = ["Juan Pérez", "María García"]
cuenta = CuentaBancaria("123456789", propietarios, 1500.0)

cuenta.mostrar_detalles()

cuenta.depositar(300)
cuenta.mostrar_detalles()

cuenta.retirar(200)
cuenta.mostrar_detalles()