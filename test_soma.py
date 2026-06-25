from app import soma
import allure

def test_soma_positiva():
    with allure.step("Somando dois números positivos"):
        resultado = soma(2,3)
    allure.attach(str(resultado), name="resultado", attachment_type=allure.attachment_type.TEXT)
    assert resultado == 5

def test_soma_negativa():
    resultado = soma(-1,-4)
    assert resultado == -5

def test_soma_valor_alto():
    resultado = soma (3500, 2550)
    assert resultado == 6050