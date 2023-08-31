def descontoINSS(sal_total):
    return sal_total * 0.11

def descontoVT(sal_total):
    return sal_total * 0.06

def descontoVA(sal_total):
    return sal_total * 0.04

def descontoTotal(inss, va, vt):
    return inss + va + vt

def salarioLiquido(sal_total, inss, va, vt):
    return sal_total - descontoTotal(inss, va, vt)

salario_bruto = float(print("Digite o salario bruto: R$"))

inss = descontoINSS(salario_bruto)
vt = descontoVT(salario_bruto)
va = descontoVA(salario_bruto)

print(f'''
INSS: R$ {inss}
VT: R$ {vt}
VA: R$ {va}
Salario Líquido: R$ {salarioLiquido(sal_total, inss, va, vt)}
''')