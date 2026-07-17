# Programa para calcular el salario neto
salario_bruto = float(input("Salario bruto: "))
porcentaje = float(input("% impuestos: "))
deducciones = float(input("Deducciones: "))
impuestos = salario_bruto * (porcentaje / 100)
salario_neto = salario_bruto - impuestos - deducciones
print("Salario neto: ", salario_neto)