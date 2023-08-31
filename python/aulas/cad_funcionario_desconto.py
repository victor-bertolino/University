def descontoINSS(sal_total):
    return sal_total * 0.11

def descontoVT(sal_total):
    return sal_total * 0.06

def descontoVA(sal_total):
    return sal_total * 0.04

def descontoTotal(inss, va, vt):
    return inss + va + vt

salario_bruto = float(print('Digite o salario bruto: R$'))

inss = descontoINSS(salario_bruto)
vt = descontoVT(salario_bruto)
va = descontoVA(salario_bruto)

print(f'''
INSS: R$ {inss}
VT: R$ {vt}
VA: R$ {va}
''')

salario_liquido = salario_bruto - descontoTotal(inss, va, vt)

print(f'Salario líquido R${salario_liquido}')

total_desconto = descontoTotal(inss, va, vt)

print(f1)
