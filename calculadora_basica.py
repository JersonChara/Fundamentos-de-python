def calculadora(a, b, operacion):
    operaciones = {
        "suma": a + b,
        "resta": a - b,
        "multiplicacion": a * b,
        "division": a / b if b !=0 else "error: division por cero",
    }
    return operaciones.get(operacion, "error: operacion no valiuda")
print(calculadora(10, 5, "suma"))
print(calculadora(10, 5, "resta"))