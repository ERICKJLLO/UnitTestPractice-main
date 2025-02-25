import pytest

from src.model.tarjeta_de_credito import TarjetaDeCredito
from src.model.compra import Compra
from src.model.error_tasa_usura import ErrorTasaUsura
from src.model.error_monto_invalido import ErrorMontoInvalido
from src.model.error_cuota_negativa import ErrorCuotaNegativa

def test_caso_36_cuotas():
    tarjeta_de_credito: TarjetaDeCredito = TarjetaDeCredito(3.1)
    compra: Compra = Compra(200000, 3.1, 36)
    tarjeta_de_credito.agregar_compra(compra)
    total_interes = tarjeta_de_credito.calcular_total_interes()
    assert total_interes == 134726.53
    
def test_Caso_24_cuotas():
    tarjeta_de_credito: TarjetaDeCredito = TarjetaDeCredito(3.4)
    compra: Compra = Compra(850000, 3.4, 24)
    tarjeta_de_credito.agregar_compra(compra)
    total_interes = tarjeta_de_credito.calcular_total_interes()
    assert total_interes == 407059.97

def test_tasa_cero():
    tarjeta_de_credito: TarjetaDeCredito = TarjetaDeCredito(0)
    compra: Compra = Compra(480000, 0, 48)
    tarjeta_de_credito.agregar_compra(compra)
    total_interes = tarjeta_de_credito.calcular_total_interes()
    assert total_interes == 0

def test_tasa_usura():
    with pytest.raises(ErrorTasaUsura):
        tarjeta_de_credito: TarjetaDeCredito = TarjetaDeCredito(12.5)
        compra: Compra = Compra(50000, 12.5, 60)
        tarjeta_de_credito.agregar_compra(compra)
        total_interes = tarjeta_de_credito.calcular_total_interes()

def test_cuota_unica():
    tarjeta_de_credito: TarjetaDeCredito = TarjetaDeCredito(2.4)
    compra: Compra = Compra(90000, 2.4, 1)
    tarjeta_de_credito.agregar_compra(compra)
    total_interes = tarjeta_de_credito.calcular_total_interes()
    assert total_interes == 0

def test_monto_invalido():
    with pytest.raises(ErrorMontoInvalido):
        tarjeta_de_credito: TarjetaDeCredito = TarjetaDeCredito(2.4)
        compra: Compra = Compra(0, 2.4, 60)
        tarjeta_de_credito.agregar_compra(compra)
        total_interes = tarjeta_de_credito.calcular_total_interes()

def test_cuota_negativa():
    with pytest.raises(ErrorCuotaNegativa):
        tarjeta_de_credito: TarjetaDeCredito = TarjetaDeCredito(1)
        compra: Compra = Compra(50000, 1, -10)
        tarjeta_de_credito.agregar_compra(compra)
        total_interes = tarjeta_de_credito.calcular_total_interes()