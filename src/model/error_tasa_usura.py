class ErrorTasaUsura:
    def __init__(self,tasa_interes: float):
        super().__init__(f"Interes de {tasa_interes}% supera la tasa de usura")