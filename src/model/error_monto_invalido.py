class ErrorMontoInvalido():
    def __init__(self, monto: float):
        super().__init__(f"El monto debe ser superior a {monto}")
        