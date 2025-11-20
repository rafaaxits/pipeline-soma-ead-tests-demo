from app import soma
import allure

def test_soma_positiva():
    with allure.step("Somando dois números positivos"):
        resultado = soma(2,3)
    allure.attach(str(resultado), name="resultado", attachment_type=allure.attachment_type.TEXT)
    assert resultado == 5

def test_soma_negativa():
    assert soma(-1,-4) == -5

def test_soma_valor_alto():
    assert soma(3500,2550) == 6050