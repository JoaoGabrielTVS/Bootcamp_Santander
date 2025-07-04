# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# TODO: Aplique o desconto se o cupom for válido:

if(cupom in list(descontos.keys()) and cupom != "SEM_DESCONTO"):
    if(list(descontos.keys())[0] == cupom):
        print("{:.2f}".format(preco - (preco * descontos.get("DESCONTO10"))))
    elif(list(descontos.keys())[1] == cupom):
        print("{:.2f}".format(preco-(preco * descontos.get("DESCONTO20"))))
    else:
        print("{:.2f}".format(preco))
