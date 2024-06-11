from validate_docbr import CPF

cpf = CPF()

print(cpf.generate(True))
print(cpf.generate(False))

print(cpf.validate('733.543.163-81'))
print(cpf.validate('40063540452'))



cpfs = [
    '40063540452',
    '733.543.163-81',
    '557.155.166-68'
]

print(cpf.validate_list(cpfs))